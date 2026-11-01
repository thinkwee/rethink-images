# rethink-images

Container images for some open-source agent projects and benchmark task sets, built from each project's official
Dockerfile and official build scripts at a pinned commit, without modification (extra layers, where there are any,
are separate and described in the workflow that builds them).

Images: `ghcr.io/thinkwee/rethink-<project>:<commit>`, `ghcr.io/thinkwee/rethink-pb-<project>:<tag>` and
`ghcr.io/thinkwee/rethink-harbor-polyglot:<language>-<hash>`.
They can also be used with singularity/apptainer via `docker://`.

Licences are those of the upstream projects:
- facebookresearch/Hyperagents (CC BY-NC-SA 4.0)
- jennyzzt/dgm (Apache-2.0)
- metauto-ai/HGM (Apache-2.0)
- harbor-framework/harbor (Apache-2.0); Aider-AI/polyglot-benchmark exercises (MIT)
