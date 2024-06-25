#!/usr/bin/env python3

"""
Script to extract channel IDs and group IDs from Microsoft Teams URLs in a text file.

The script reads a text file containing Microsoft Teams URLs, extracts the channel ID
and group ID from each URL, and outputs the results in various formats.

Input:
- Text file containing Microsoft Teams URLs, one URL per line.

Output:
- Comma-separated list of group ID and channel ID pairs (default).
- Comma-separated list of channel IDs.
- Comma-separated list of group IDs.
- JSON object with group IDs as keys and channel IDs as values.

Usage:
    ./extract_ids.py --file path/to/yourfile.txt --output output_format

Arguments:
    --file      Path to the file containing URLs. Default is "channels.txt".
    --output    Output format: "pair", "channels", "groups", "json". Default is "pair".

Example:
    ./extract_ids.py --file channels.txt --output json
"""

import argparse
import urllib.parse
import re
import json

def parse_url(url):
    """
    Parses a Microsoft Teams URL to extract the channel ID and group ID.
    
    Args:
        url (str): The URL to be parsed.
        
    Returns:
        tuple: A tuple containing the group ID and channel ID.
    """
    try:
        pattern = re.compile(r'/channel/([^/]+)/.*groupId=([^&]+)')
        match = pattern.search(url)
        if match:
            encoded_channel_id = match.group(1)
            channel_id = urllib.parse.unquote(encoded_channel_id)
            group_id = match.group(2)
            return group_id, channel_id
        else:
            return None, None
    except Exception as e:
        print(f"Error parsing URL {url}: {e}")
        return None, None

def read_file(file_path):
    """
    Reads a file and returns its contents as a list of lines, excluding comments (#).
    
    Args:
        file_path (str): Path to the file.
        
    Returns:
        list: List of non-comment lines from the file.
    """
    try:
        with open(file_path, 'r') as file:
            # Filter out lines that start with "#" (comments)
            return [line for line in file if not line.strip().startswith("#")]
    except FileNotFoundError:
        print(f"Warning: File {file_path} not found.")
        return []
    except IOError:
        print(f"Warning: Could not read file {file_path}.")
        return []

def main(file, output):
    """
    Main function to process the URLs and output the results in the specified format.
    
    Args:
        file (str): Path to the file containing URLs.
        output (str): Output format: "pair", "channels", "groups", "json".
    """
    urls = read_file(file)
    results = [parse_url(url.strip()) for url in urls]

    if output == "channels":
        # Output a comma-separated list of channel IDs
        channels = [channel for _, channel in results if channel]
        print(",".join(channels))
    elif output == "groups":
        # Output a comma-separated list of group IDs
        groups = [group for group, _ in results if group]
        print(",".join(groups))
    elif output == "json":
        # Output a JSON array of objects with group IDs and channel IDs
        data = [{"group_id": group, "channel_id": channel} for group, channel in results if group and channel]
        print(json.dumps(data, indent=4))
    else:  # default to "pair"
        # Output a comma-separated list of group ID and channel ID pairs
        pairs = [f"{group};{channel}" for group, channel in results if group and channel]
        print(",".join(pairs))

if __name__ == "__main__":
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(
        description='Extract channel ID and group ID from Microsoft Teams URLs.',
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument('--file', type=str, default="channels.txt", help='Path to the file containing URLs.')
    parser.add_argument(
        '--output', type=str, choices=['glean', 'channels', 'groups', 'json'], default="glean",
        help='Output format:\n'
             '"glean" - Comma-separated list of `group ID;channel ID` pairs (default).\n'
             '"channels" - Comma-separated list of channel IDs.\n'
             '"groups" - Comma-separated list of group IDs.\n'
             '"json" - JSON array of objects with group IDs and channel IDs.'
    )
    args = parser.parse_args()
    
    # Call the main function with the parsed arguments
    main(args.file, args.output)
