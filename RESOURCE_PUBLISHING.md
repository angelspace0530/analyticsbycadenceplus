# CadencePlus Solutions™ | Resource Publishing Guide

This repository is a **growing public learning resource library**, not a repository dedicated to one Kora pack. The `project packs/` directory is one resource category. Project packs may belong to collections (such as Kora) and every individual pack has its own unique identity.

## Current structure and compatibility

The existing published path `project packs/Kora - 2025 only/` must remain stable because published URLs may reference it. **Do not move or rename it without a deliberate link migration.** Future folders can be organised more consistently, but folder structure must not determine the entire public catalogue.

Kora has **four intended project packs**. Only `Kora - 2025 only` is published in the current repository. Do not invent names, downloads, or published status for the remaining packs.

## Publishing a new resource

1. Decide the category (project pack, guide, template, dataset, or a new type).
2. For project packs, identify an existing collection or create a new collection ID. Each pack gets a unique, stable resource ID.
3. Add the actual resource files to an appropriately named folder. Prefer a complete ZIP for multi-file packs and a clearly labelled main guide.
4. For SQL-based packs, include local setup files, data, a data dictionary, validation scripts and platform-specific instructions as applicable.
5. Test every setup path and check that the ZIP contents match the published standalone files.
6. Add a **published** entry to `resources.json` only when the files and download paths exist. Update the collection's published count, and add new categories or collections as required.
7. Add or update a human-readable link from the root README. Ensure paths with spaces are URL-encoded in Markdown links.
8. Verify the guide opens, ZIP downloads, resource links work and any scripts execute on the stated platforms before announcing availability.

## Catalogue conventions

`resources.json` is the machine-readable index. It uses:

- `schema_version`: catalogue format version.
- `categories`: open-ended resource types with stable IDs.
- `collections`: optional resource families (for example, Kora), distinct from the packs they contain.
- `resources`: one entry per individually publishable resource, with `id`, `category_id`, `status`, `access`, `root_path` and `files`.
- `collection_id`: optional reference to an existing collection.
- `files`: repository-relative paths, not fabricated download URLs.

Treat resource IDs as permanent identifiers. Do not infer availability from a folder name; only entries with `status: "published"` and valid file paths should appear in a public resource listing. When a pack is revised, update its version and test its download again. Use explicit archived status for withdrawn entries, with a replacement link where available. If a future application needs drafts, use a separate private editorial store; the public catalogue should not expose unpublished sensitive material.

`planned_pack_count` is informational. It is not a reason to display four live download cards or invent three placeholder names.

## Website and Learning Hub integration

A site can read this catalogue and render categories, collections and pack detail cards dynamically. Resolve file paths relative to the repository, handle URL encoding safely, and show only published items. Avoid hardcoded Kora-specific resource counts and paths. **A catalogue is metadata, not access control.**

Never place private learner information, secrets, licensed third-party datasets without permission, or **paid Jathan downloads** in this public GitHub repository. Paid files require private storage and server-enforced entitlements.

## Quality checks before every release

- [ ] Title, description, category, collection and intended audience are accurate
- [ ] Real files exist for every catalogue file path
- [ ] PDF and ZIP downloads open correctly
- [ ] Setup scripts work for the stated tools and operating systems
- [ ] Files and datasets contain no personal, sensitive or secret information
- [ ] Licence, attribution and synthetic-data disclaimers are accurate
- [ ] Existing published download URLs still work
- [ ] README and catalogue reflect the released pack
