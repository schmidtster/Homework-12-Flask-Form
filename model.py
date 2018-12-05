import json
from datetime import datetime

GUESTBOOK_ENTRIES_FILE = "entries.json"
entries = []
next_id = 0


def init():
    global entries, next_id
    try:
        f = open(GUESTBOOK_ENTRIES_FILE)
        entries = json.loads(f.read())
        previous_id = entries[0]["postid"]
        next_id = int(previous_id) + 1
        f.close()
    except:
        entries = []


def get_entries():
    global entries
    return entries


def add_entry(name, text):
    global entries, GUESTBOOK_ENTRIES_FILE, next_id
    now = datetime.now()
    time_string = str(now)
    # if you have an error using this format, just use
    # time_string = str(now)
    entry = {"author": name, "text": text, "timestamp": time_string, "postid": str(next_id)}
    entries.insert(0, entry)  # add to front of list
    next_id += 1
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")


def delete_entry(postid):
    global entries, GUESTBOOK_ENTRIES_FILE
    print(entries)
    entries = [entry for entry in entries if entry.get("postid") != postid]
    print(entries)
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")


# def edit_entry(postid, text):
#     global entries, GUESTBOOK_ENTRIES_FILE
#     for entry in entries:
#         if entry["postid"] == postid:
#             add_entry(entry["name"], text)
#     try:
#         f = open(GUESTBOOK_ENTRIES_FILE, "w")
#         dump_string = json.dumps(entries)
#         f.write(dump_string)
#         f.close()
#     except:
#         print("ERROR! Could not write entries to file.")
