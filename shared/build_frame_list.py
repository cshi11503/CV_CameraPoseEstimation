
from pathlib import Path
import argparse
import json
import yaml


def load_config(config_path):
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def build_frame_list(config, stride):
    dataset = config["dataset"]
    sampling = config["sampling"]

    root = Path(dataset["root"])
    scene = dataset["scene"]
    sequence = dataset["sequence"]

    n = sampling["num_images"]
    start = sampling["start_frame"]

    sequence_dir = root / scene / sequence
    frame_ids = [start + i * stride for i in range(n)]

    frames = []

    for frame_id in frame_ids:
        image_path = sequence_dir / f"frame-{frame_id:06d}.color.png"

        if not image_path.is_file():
            raise FileNotFoundError(
                f"Missing image: {image_path}\n"
                "Check the dataset path and extracted sequence."
            )

        frames.append({
            "frame_index": frame_id,
            "image_path": str(image_path.resolve())
        })

    return frames


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--config",
        default="configs/experiment.yaml"
    )
    parser.add_argument(
        "--output-dir",
        default="data/frame_lists"
    )
    args = parser.parse_args()

    config = load_config(args.config)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    scene = config["dataset"]["scene"]
    sequence = config["dataset"]["sequence"]
    n = config["sampling"]["num_images"]

    for stride in config["sampling"]["strides"]:
        frames = build_frame_list(config, stride)

        filename = (
            f"{scene}_{sequence}_s{stride}_n{n}.json"
        )

        output_path = output_dir / filename

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(frames, f, indent=2)

        print(
            f"Stride {stride:2d}: "
            f"{len(frames)} frames, "
            f"{frames[0]['frame_index']} -> "
            f"{frames[-1]['frame_index']}"
        )

        print(f"  Saved: {output_path}")


if __name__ == "__main__":
    main()
