#!/bin/bash

# Copyright (c) 2023 MDSANIMA

# This script renames all Git tags based on the mapping defined in an
# associative array. The new tags will replace the old tags in the same
# locations in commit history. You need to edit this file and specify
# which tags you want to rename.


# Define the mapping of old tags to new ones
declare -A tag_map
tag_map["0.1.0"]="v0.1.0"
tag_map["0.1.1"]="v0.1.1"
tag_map["0.1.2"]="v0.1.2"
tag_map["0.1.3"]="v0.1.3"
tag_map["0.2.0"]="v0.2.0"
tag_map["0.2.1"]="v0.2.1"

# Iterate through all tags in the mapping
for old_tag in "${!tag_map[@]}"; do
  new_tag=${tag_map[$old_tag]}

  # Get the SHA commit for the old tag
  commit_sha=$(git rev-list -n 1 $old_tag)

  # Delete the old tag locally
  git tag -d $old_tag

  # Add a new tag
  git tag $new_tag $commit_sha

  # Delete the old tag from the origin
  git push origin :refs/tags/$old_tag

  # Push the new tag to the origin
  git push origin $new_tag
done
