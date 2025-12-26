#!/usr/bin/env python3
"""
Manim Build Script
编译和渲染 Manim 场景为视频文件

输出结构:
manim_outputs/
└── <scene_name>_<timestamp>/
    ├── scene.py                   # 源代码
    ├── config.json                # 生成配置
    ├── output/
    │   └── <quality>/
    │       └── <SceneName>.mp4
    ├── logs/
    │   ├── build.log
    │   └── manim.log
    └── README.md

使用方法:
    python build.py scene.py MyScene
    python build.py scene.py MyScene --quality high
"""

import argparse
import json
import os
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

# 质量配置映射
QUALITY_MAP = {
    "low": {
        "flag": "-ql",
        "name": "480p",
        "resolution": "854x480",
        "frame_rate": 15
    },
    "medium": {
        "flag": "-qm",
        "name": "720p",
        "resolution": "1280x720",
        "frame_rate": 30
    },
    "high": {
        "flag": "-qh",
        "name": "1080p",
        "resolution": "1920x1080",
        "frame_rate": 30
    },
    "4k": {
        "flag": "-qk",
        "name": "2160p",
        "resolution": "3840x2160",
        "frame_rate": 60
    }
}

# 输出基础目录
OUTPUT_BASE_DIR = Path("manim_outputs")


def check_manim_installed():
    """检查 manim 是否已安装"""
    try:
        result = subprocess.run(
            ["manim", "--version"],
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.returncode == 0
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return False


def create_output_structure(scene_name: str, quality: str, description: str = "") -> Path:
    """
    创建输出目录结构

    Args:
        scene_name: 场景名称
        quality: 质量级别
        description: 场景描述

    Returns:
        Path: 输出目录路径
    """
    # 生成时间戳
    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")

    # 创建输出目录: manim_outputs/<scene_name>_<timestamp>/
    output_dir = OUTPUT_BASE_DIR / f"{scene_name}_{timestamp}"
    output_dir.mkdir(parents=True, exist_ok=True)

    # 创建子目录
    (output_dir / "output" / quality).mkdir(parents=True, exist_ok=True)
    (output_dir / "logs").mkdir(exist_ok=True)
    (output_dir / "thumbnails").mkdir(exist_ok=True)

    # 保存配置
    config = {
        "scene_name": scene_name,
        "quality": quality,
        "description": description,
        "timestamp": timestamp,
        "created_at": datetime.now().isoformat(),
        "manim_version": get_manim_version()
    }

    with open(output_dir / "config.json", "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2, ensure_ascii=False)

    # 生成 README.md
    readme_content = f"""# {scene_name}

生成时间: {timestamp}

## 配置
- 质量: {quality}
- 分辨率: {QUALITY_MAP[quality]['resolution']}

## 文件说明
- `scene.py`: Manim 源代码
- `output/{quality}/`: 视频输出目录
- `logs/`: 编译日志
- `config.json`: 生成配置
"""

    with open(output_dir / "README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)

    return output_dir


def get_manim_version():
    """获取 manim 版本"""
    try:
        result = subprocess.run(
            ["manim", "--version"],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            return result.stdout.strip()
    except:
        pass
    return "unknown"


def copy_scene_file(scene_file: Path, output_dir: Path):
    """复制场景文件到输出目录"""
    dest = output_dir / "scene.py"
    shutil.copy2(scene_file, dest)
    print(f"📄 源代码已复制: {dest}")


def build_scene(
    scene_file: str,
    scene_name: str = "Scene",
    quality: str = "high",
    description: str = "",
    custom_output_dir: str = None
) -> tuple[bool, Path]:
    """
    编译 Manim 场景

    Args:
        scene_file: Scene .py 文件路径
        scene_name: 场景类名
        quality: 渲染质量
        description: 场景描述
        custom_output_dir: 自定义输出目录（覆盖默认行为）

    Returns:
        (success, output_dir): 是否成功和输出目录路径
    """
    scene_path = Path(scene_file)

    # 检查文件是否存在
    if not scene_path.exists():
        print(f"❌ 错误: 找不到文件 '{scene_file}'")
        return False, None

    # 检查 manim 是否安装
    if not check_manim_installed():
        print("❌ 错误: manim 未安装")
        print("   请运行: pip install manim")
        return False, None

    # 验证质量参数
    if quality not in QUALITY_MAP:
        print(f"❌ 错误: 无效的质量参数 '{quality}'")
        print(f"   可选: {', '.join(QUALITY_MAP.keys())}")
        return False, None

    # 创建输出目录结构
    if custom_output_dir:
        output_dir = Path(custom_output_dir)
    else:
        output_dir = create_output_structure(scene_name, quality, description)

    # 复制场景文件
    copy_scene_file(scene_path, output_dir)

    quality_config = QUALITY_MAP[quality]
    quality_flag = quality_config["flag"]

    # 构建 manim 命令，输出到指定目录
    manim_output_dir = output_dir / "output"
    cmd = ["manim", quality_flag, "-o", str(manim_output_dir), str(scene_path), scene_name]

    print(f"🎬 编译场景: {scene_name}")
    print(f"📁 输出目录: {output_dir}")
    print(f"🎨 质量: {quality} ({quality_config['resolution']})")
    print("-" * 50)

    try:
        # 运行 manim 命令
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=300  # 5 分钟超时
        )

        # 保存编译日志
        log_file = output_dir / "logs" / "build.log"
        with open(log_file, "w", encoding="utf-8") as f:
            f.write(f"Command: {' '.join(cmd)}\n\n")
            f.write(f"STDOUT:\n{result.stdout}\n\n")
            f.write(f"STDERR:\n{result.stderr}\n")

        if result.returncode == 0:
            print("✅ 编译成功!")

            # 查找生成的视频文件
            video_file = find_output_video(manim_output_dir, scene_name, quality)
            if video_file:
                print(f"\n📺 视频文件: {video_file}")
                print(f"📂 完整输出: {output_dir}")
                return True, output_dir
            else:
                print("⚠️  编译成功但未找到视频文件")
                return True, output_dir
        else:
            print("❌ 编译失败!")
            print(result.stderr)
            print(f"\n📋 查看日志: {log_file}")
            return False, output_dir

    except subprocess.TimeoutExpired:
        print("❌ 错误: 编译超时（超过 5 分钟）")
        print("   建议: 使用较低质量或简化场景")
        return False, output_dir
    except Exception as e:
        print(f"❌ 错误: {e}")
        return False, output_dir


def find_output_video(output_dir: Path, scene_name: str, quality: str) -> Path:
    """
    查找输出的视频文件

    Args:
        output_dir: Manim 输出目录
        scene_name: 场景名称
        quality: 质量级别

    Returns:
        Path: 视频文件路径，如果找不到则返回 None
    """
    quality_name = QUALITY_MAP[quality]["name"]

    # 可能的视频文件路径
    possible_names = [
        f"{scene_name}.mp4",
        f"{scene_name.capitalize()}.mp4",
    ]

    for name in possible_names:
        video_path = output_dir / quality_name / name
        if video_path.exists():
            return video_path

        # 也检查直接在 output 目录下
        video_path = output_dir / name
        if video_path.exists():
            return video_path

    # 递归查找所有 .mp4 文件
    mp4_files = list(output_dir.glob("**/*.mp4"))
    if mp4_files:
        return mp4_files[0]

    return None


def export_to_gif(input_mp4: str, output_dir: Path, fps: int = 30, scale: float = 1.0):
    """
    将 MP4 转换为 GIF

    Args:
        input_mp4: 输入 MP4 文件路径
        output_dir: 输出目录
        fps: 帧率
        scale: 缩放比例
    """
    if not Path(input_mp4).exists():
        print(f"❌ 错误: 找不到文件 '{input_mp4}'")
        return False

    output_gif = output_dir / "thumbnails" / Path(input_mp4).with_suffix(".gif").name

    # 检查 ffmpeg 是否可用
    try:
        subprocess.run(
            ["ffmpeg", "-version"],
            capture_output=True,
            timeout=5
        )
    except (FileNotFoundError, subprocess.TimeoutExpired):
        print("❌ 错误: ffmpeg 未安装")
        print("   安装: sudo apt-get install ffmpeg")
        return False

    # 构建 ffmpeg 命令
    scale_filter = f"scale=iw*{scale}:ih*{scale}"
    cmd = [
        "ffmpeg", "-i", input_mp4,
        "-vf", f"{scale_filter},fps={fps}",
        "-y", str(output_gif)
    ]

    try:
        print(f"🎞️  转换为 GIF: {output_gif}")
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)

        if result.returncode == 0:
            print("✅ 转换成功!")
            print(f"📁 GIF 文件: {output_gif}")
            return True
        else:
            print("❌ 转换失败!")
            print(result.stderr)
            return False

    except subprocess.TimeoutExpired:
        print("❌ 错误: 转换超时")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Manim 场景编译脚本",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s scene.py MyScene
  %(prog)s scene.py MyScene --quality high
  %(prog)s scene.py MyScene --format gif
        """
    )

    parser.add_argument("file", help="Scene .py 文件路径")
    parser.add_argument("--scene", default="Scene", help="场景类名（默认: Scene）")
    parser.add_argument(
        "--quality",
        choices=["low", "medium", "high", "4k"],
        default="high",
        help="渲染质量（默认: high / 1080p）"
    )
    parser.add_argument(
        "--description",
        default="",
        help="场景描述"
    )
    parser.add_argument(
        "--format",
        choices=["mp4", "gif", "png"],
        default="mp4",
        help="输出格式（默认: mp4）"
    )
    parser.add_argument("--output", help="自定义输出目录（覆盖默认组织结构）")

    args = parser.parse_args()

    # 编译场景
    success, output_dir = build_scene(
        scene_file=args.file,
        scene_name=args.scene,
        quality=args.quality,
        description=args.description,
        custom_output_dir=args.output
    )

    if not success:
        sys.exit(1)

    # 如果需要 GIF 转换
    if args.format == "gif" and output_dir:
        video_file = find_output_video(output_dir / "output", args.scene, args.quality)
        if video_file:
            export_to_gif(str(video_file), output_dir)

    sys.exit(0)


if __name__ == "__main__":
    main()
