from dataclasses import dataclass

from .detection import Ball


@dataclass(frozen=True)
class TrackingResult:
    frame_index: int
    time_seconds: float
    ball: Ball | None

    @property
    def status(self) -> str:
        return "visible" if self.ball is not None else "lost"


class Tracker:
    def __init__(self) -> None:
        self._last_detection: Ball | None = None

    def update(self, frame_index: int, fps: float, detection: Ball | None) -> TrackingResult:
        if detection is not None:
            self._last_detection = detection
        return TrackingResult(frame_index, frame_index / fps, self._last_detection)
