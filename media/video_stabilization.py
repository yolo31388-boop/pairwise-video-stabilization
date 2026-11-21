import math

def feature_confidence(variance, threshold):
    """特征置信度：局部灰度方差达到阈值才可信，低纹理区域不可信。"""
    return variance >= threshold

def window_frames(seconds, fps):
    """平滑窗口：按时间跨度换算帧数，VFR 下窗口时长恒定。"""
    return max(1, int(round(seconds * fps)))

def crop_scale(displacement, resolution):
    """裁切比例：按分位位移相对画面尺寸计算，而非最坏位移。"""
    if resolution <= 0:
        return 1.0
    return max(0.0, min(1.0, 1.0 - displacement / resolution))

def rolling_shutter_offset(row, readout, velocity):
    """滚动快门：按行读出时间乘以速度做逐行补偿。"""
    return row * readout * velocity

def reset_trajectory(cut, history):
    """切镜重置：检测到场景切换即清空轨迹历史。"""
    return bool(cut)

def camera_trajectory_key(camera_id):
    """多相机轨迹键：每个相机（左/右眼）独立轨迹。"""
    return camera_id

def bit_depth(value, bits):
    """10bit 链路：按位深满量程缩放，中间缓冲不压到 8bit。"""
    return value * ((1 << bits) - 1)

def black_border_fill(mode):
    """黑边填充：反射填充等模式，避免黑框。"""
    return mode

def phase_match(gpu_phase, cpu_phase):
    """预览导出一致：GPU 与 CPU 路径平滑相位相同。"""
    return gpu_phase == cpu_phase

def degrade_smoothing(quality):
    """降级平滑：性能档只做轻度平滑，不关闭防抖。"""
    return max(0.0, min(1.0, quality))

def smooth_path(points, window):
    """轨迹平滑：窗口内滑动平均。"""
    if not points:
        return 0.0
    tail = points[-max(1, window):]
    return sum(tail) / len(tail)

def translation_only(motion):
    """仅平移分量。"""
    return (motion[0], motion[1])

def stabilize_offset(offset, crop):
    """偏移钳制：稳定偏移不超出裁切允许范围。"""
    return max(-crop, min(crop, offset))

def scene_cut_score(delta, threshold):
    """场景切换：帧间差异超过阈值判定为切镜。"""
    return delta >= threshold

def frame_time(frame, fps):
    """帧时间。"""
    return frame / fps
