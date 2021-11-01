from __future__ import annotations

import typing as ty

from PyQt5.QtCore import QEasingCurve, QPropertyAnimation
from PyQt5.QtGui import QIcon

if ty.TYPE_CHECKING:
    from PyQt5.QtWidgets import QPushButton
    from main_window import MainWindow


def buttonsHandler(main_window: MainWindow, button: QPushButton) -> None:
    """
    Обработчик кнопок панели управления.
    :param main_window: Экземпляр главного окна.
    :param button: Нажатая кнопка.
    """
    if button == main_window.speedBtn:
        toggleSpeedSlider(main_window)
    elif button == main_window.volumeBtn:
        toggleVolumeSlider(main_window)


def toggleSpeedSlider(main_window: MainWindow) -> None:
    """
    Показывает/скрывает регулятор скорости.
    :param main_window: Экземпляр главного окна.
    """
    if not main_window.__dict__.get(
        "speed_frame_animation"
    ) and not main_window.__dict__.get("volume_frame_animation"):
        if main_window.volumeFrame.minimumWidth() != 0:
            toggleVolumeSlider(main_window)

        width = main_window.speedFrame.width()  # Ширина виджета сейчас
        # Конечная ширина виджета. 110-открытое 65-закрытое
        end_value = 120 if width == 0 else 0

        main_window.speed_frame_animation = QPropertyAnimation(
            main_window.speedFrame, b"minimumWidth"
        )
        main_window.speed_frame_animation.setDuration(150)
        main_window.speed_frame_animation.setStartValue(width)
        main_window.speed_frame_animation.setEndValue(end_value)
        main_window.speed_frame_animation.setEasingCurve(QEasingCurve.InOutQuart)
        main_window.speed_frame_animation.finished.connect(
            lambda: main_window.__dict__.__delitem__("speed_frame_animation")
        )  # Удаляем анимацию
        main_window.speed_frame_animation.start()


def toggleVolumeSlider(main_window: MainWindow) -> None:
    """
    Показывает/скрывает регулятор громкости.
    :param main_window: Экземпляр главного окна.
    """
    if not main_window.__dict__.get(
        "volume_frame_animation"
    ) and not main_window.__dict__.get("speed_frame_animation"):
        if main_window.speedFrame.minimumWidth() != 0:
            toggleSpeedSlider(main_window)

        width = main_window.volumeFrame.width()  # Ширина виджета сейчас
        # Конечная ширина виджета 110-открытое 65-закрытое
        end_value = 120 if width == 0 else 0

        main_window.volume_frame_animation = QPropertyAnimation(
            main_window.volumeFrame, b"minimumWidth"
        )
        main_window.volume_frame_animation.setDuration(150)
        main_window.volume_frame_animation.setStartValue(width)
        main_window.volume_frame_animation.setEndValue(end_value)
        main_window.volume_frame_animation.setEasingCurve(QEasingCurve.InOutQuart)
        main_window.volume_frame_animation.finished.connect(
            lambda: main_window.__dict__.__delitem__("volume_frame_animation")
        )  # Удаляем анимацию
        main_window.volume_frame_animation.start()


def volumeSliderHandler(main_window: MainWindow, value: int) -> None:
    """
    Обработчик изменений значения слайдера громкости.
    :param main_window: Экземпляр главного окна.
    :param value: Новое значение.
    """
    main_window.volumeLabel.setText(f"{value} %")

    # Изменяем иконку кнопки
    if value == 0:
        icon = QIcon(":/volume/mute.svg")
    elif value < 33:
        icon = QIcon(":/volume/low_volume.svg")
    elif 33 < value < 70:
        icon = QIcon(":/volume/medium_volume.svg")
    elif value > 70:
        icon = QIcon(":/volume/volume.svg")
    else:
        icon = main_window.volumeBtn.icon()
    main_window.volumeBtn.setIcon(icon)

    main_window.player.player.setVolume(value)


def speedSliderHandler(main_window: MainWindow, value: int) -> None:
    """
    Обработчик изменений значения слайдера скорости.
    :param main_window: Экземпляр главного окна.
    :param value: Новое значение.
    """
    value = value // 5 * 5
    value = 1 + value / 50

    main_window.speedLabel.setText(f"x{value}")
    main_window.player.player.setPlaybackRate(value)
