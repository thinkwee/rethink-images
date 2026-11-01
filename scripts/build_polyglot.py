"""Build the Polyglot evaluation images exactly as the official code builds them, then list the tags.

Run from the root of the official repo (dgm, HGM or Hyperagents) after its official dataset preparation step.
Uses the official build functions unchanged: <pkg>.docker_build.build_instance_images builds the base image,
the environment images and one instance image per exercise.
"""
import importlib, json, sys
import docker

pkg, meta_path = sys.argv[1], sys.argv[2]
db = importlib.import_module(f"{pkg}.docker_build")
dataset = json.load(open(meta_path))
print(f"{len(dataset)} instances in {meta_path}")
client = docker.from_env()
res = db.build_instance_images(client, dataset, force_rebuild=False, max_workers=4)
print("build result:", res if not isinstance(res, tuple) else [len(x) for x in res])
tags = sorted(t for img in client.images.list() for t in img.tags if t.startswith("pb."))
json.dump(tags, open("pb_tags.json", "w"), indent=1)
print(f"{len(tags)} pb.* tags")
