# rethink-images

Container images for several open-source recursive self-improvement (RSI) agent projects, built from each project's
official Dockerfile and official build scripts at a pinned commit, without modification.

Images: `ghcr.io/thinkwee/rethink-<project>:<commit>` and `ghcr.io/thinkwee/rethink-pb-<project>:<tag>`.
They can also be used with singularity/apptainer via `docker://`.

Licences are those of the upstream projects:
- facebookresearch/Hyperagents (CC BY-NC-SA 4.0)
- jennyzzt/dgm (Apache-2.0)
- metauto-ai/HGM (Apache-2.0)
