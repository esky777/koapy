import inspect
import threading

from koapy.backend.kiwoom_open_api_plus.core.KiwoomOpenApiPlusSignature import (
    KiwoomOpenApiPlusEventHandlerSignature,
)
from koapy.backend.kiwoom_open_api_plus.utils.list_type import string_to_list
from koapy.compat.pyside2 import PYQT5, PYSIDE2, PythonQtError
from koapy.utils.logging.Logging import Logging


class KiwoomOpenApiPlusSignalConnector(Logging):
    def __init__(self, name):
        super().__init__()

        self._name = name
        self._lock = threading.RLock()
        self._slots = list()

        self._signature = KiwoomOpenApiPlusEventHandlerSignature.from_name(self._name)
        self._param_types = [
            (p.annotation) for p in self._signature.parameters.values()
        ]

        if PYSIDE2:
            self._signal = self._signature.to_pyside2_event_signal()

        self.__name__ = self._name

    def is_valid_slot(self, slot):
        slot_signature = inspect.signature(slot)
        slot_types = [(p.annotation) for p in slot_signature.parameters.values()]
        condition = len(self._param_types) == len(
            slot_types
        )  # currently only check parameter length
        return condition

    def connect_to(self, control):
        if PYSIDE2:
            return control.connect(self._signal, self)
        elif PYQT5:
            return getattr(control, self._name).connect(self)
        else:
            raise PythonQtError("Unsupported Qt bindings")

    def connect(self, slot):
        if not self.is_valid_slot(slot):
            raise ValueError("Tried to connect invalid slot: %s" % slot)
        with self._lock:
            if slot not in self._slots:
                self._slots.append(slot)

    def disconnect(self, slot=None):
        with self._lock:
            if slot is None:
                self._slots.clear()
            elif slot in self._slots:
                self._slots.remove(slot)
            else:
                self.logger.warning("Tried to disconnect a slot that doesn't exist")

    def call(self, *args, **kwargs):
        # make a copy in order to prevent modification during iteration problem
        with self._lock:
            slots = list(self._slots)
        # TODO: use Thread with await/join for concurrency?
        for slot in slots:
            slot(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        return self.call(*args, **kwargs)


class KiwoomOpenApiPlusOnReceiveRealDataSignalConnector(
    KiwoomOpenApiPlusSignalConnector
):
    def __init__(self, control):
        super().__init__("OnReceiveRealData")
        self._control = control
        self._pending_removes = {}
        self._pending_removes_lock = threading.RLock()

        self._SetRealReg = self._control.SetRealReg
        self._SetRealRemove = self._control.SetRealRemove

    def SetRealReg(self, screen_no, code_list, fid_list, opt_type):
        if self._pending_removes:
            with self._pending_removes_lock:
                code_list_split = string_to_list(code_list)
                for code in code_list_split:
                    if code in self._pending_removes:
                        if screen_no in self._pending_removes[code]:
                            self._pending_removes[code].remove(screen_no)
        return self._SetRealReg(screen_no, code_list, fid_list, opt_type)

    def SetRealRemove(self, screen_no, code):
        if "ALL" in (screen_no, code):
            return self._SetRealRemove(screen_no, code)
        with self._pending_removes_lock:
            self._pending_removes.setdefault(code, []).append(screen_no)
            return

    def call(self, code, realtype, realdata):  # pylint: disable=arguments-differ
        super().call(code, realtype, realdata)
        if self._pending_removes:
            with self._pending_removes_lock:
                if code in self._pending_removes:
                    for screen_no in self._pending_removes[code]:
                        self._SetRealRemove(screen_no, code)
                    del self._pending_removes[code]