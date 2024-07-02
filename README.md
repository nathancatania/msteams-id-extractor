# msteams-id-extractor
Simple script to extract Channel IDs and/or Team/Group IDs from a list of Microsoft Teams Channel URLs.

All channel and group IDs automatically have any URL encoding reverted (if applicable).

## Requirements
* Python 3

## Usage
By default the script looks for a file in the same directory called `channels.txt` to parse. You can specify a different filename/path using the `--file` argument.

1. Add a list of Teams Channel URLs to a `txt` file. Save the file as `channels.txt`.

    * Each URL should be on a newline.
    * See `channels.txt` in the repository for an example.

2. Run the script:

    ```
    python extract-teams.py
    ```

    Alternatively with a different file/filepath:
    ```
    python extract-teams.py --file ~/folder/my_channel_urls.txt
    ```

3. Review the output (see below for changing the format):
    ```
    b8fe8e94-51bc-4ba8-869a-cac1fba25370;19:sbe3kFzquLgN3NmBVwJf-sf8xjHJIjcPUn1gW6UjLKc1@thread.tacv2,b8fe8e94-51bc-4ba8-869a-cac1fba25370;19:6d3c7107e87d438ba488b291967cde27@thread.tacv2,b8fe8e94-51bc-4ba8-869a-cac1fba25370;19:f7686e91aaf04a708cbb5fcd426667b6@thread.tacv2,7c77e355-c78c-4362-b195-d2428e285106;19:QP8HwjdClK-pQgDB3nlB16FJJmn2M2-Y36tOWAOREXc1@thread.tacv2,c6eff061-b1c0-4cc4-90d9-b4b029c7af8f;19:Sc-geobTNwKjd8aE6gw73S1Ij1QpLXIL6iolH7MjhHI1@thread.tacv2,c6eff061-b1c0-4cc4-90d9-b4b029c7af8f;19:3f341a2ee6d44358a3c0bb7e824a993a@thread.tacv2
    ```

## Output Formats
You can specify alternative output formats using the `--output` flag:

* `glean` (default)
* `json`
* `channels`
* `groups`

### Glean (default)
The default format is to output to a `<group_id>,<channel_id>` semi-comma-separated pair used for Glean, e.g.
```
<group_id1>,<channel_id1>;<group_id1>,<channel_id2>;<group_id2>,<channel_id1>; ...
```

### JSON
The `json` output format will print a list of JSON dictionaries that can be iterated over.

```
python extract-teams.py --output json
[
    {
        "group_id": "b8fe8e94-51bc-4ba8-869a-cac1fba25370",
        "channel_id": "19:sbe3kFzquLgN3NmBVwJf-sf8xjHJIjcPUn1gW6UjLKc1@thread.tacv2"
    },
    {
        "group_id": "b8fe8e94-51bc-4ba8-869a-cac1fba25370",
        "channel_id": "19:6d3c7107e87d438ba488b291967cde27@thread.tacv2"
    },
    {
        "group_id": "b8fe8e94-51bc-4ba8-869a-cac1fba25370",
        "channel_id": "19:f7686e91aaf04a708cbb5fcd426667b6@thread.tacv2"
    },
    {
        "group_id": "7c77e355-c78c-4362-b195-d2428e285106",
        "channel_id": "19:QP8HwjdClK-pQgDB3nlB16FJJmn2M2-Y36tOWAOREXc1@thread.tacv2"
    },
    {
        "group_id": "c6eff061-b1c0-4cc4-90d9-b4b029c7af8f",
        "channel_id": "19:Sc-geobTNwKjd8aE6gw73S1Ij1QpLXIL6iolH7MjhHI1@thread.tacv2"
    },
    {
        "group_id": "c6eff061-b1c0-4cc4-90d9-b4b029c7af8f",
        "channel_id": "19:3f341a2ee6d44358a3c0bb7e824a993a@thread.tacv2"
    }
]
```

### Channels
The `channels` output format will simply print a comma-separated list of just the Channel IDs.

```
extract-teams.py --output channels

19:sbe3kFzquLgN3NmBVwJf-sf8xjHJIjcPUn1gW6UjLKc1@thread.tacv2,19:6d3c7107e87d438ba488b291967cde27@thread.tacv2,19:f7686e91aaf04a708cbb5fcd426667b6@thread.tacv2,19:QP8HwjdClK-pQgDB3nlB16FJJmn2M2-Y36tOWAOREXc1@thread.tacv2,19:Sc-geobTNwKjd8aE6gw73S1Ij1QpLXIL6iolH7MjhHI1@thread.tacv2,19:3f341a2ee6d44358a3c0bb7e824a993a@thread.tacv2
```

### Groups
The `groups` output format will simply print a comma-separated list of just the Teams/Group IDs:

```
extract-teams.py --output channels

19:sbe3kFzquLgN3NmBVwJf-sf8xjHJIjcPUn1gW6UjLKc1@thread.tacv2,19:6d3c7107e87d438ba488b291967cde27@thread.tacv2,19:f7686e91aaf04a708cbb5fcd426667b6@thread.tacv2,19:QP8HwjdClK-pQgDB3nlB16FJJmn2M2-Y36tOWAOREXc1@thread.tacv2,19:Sc-geobTNwKjd8aE6gw73S1Ij1QpLXIL6iolH7MjhHI1@thread.tacv2,19:3f341a2ee6d44358a3c0bb7e824a993a@thread.tacv2
```
