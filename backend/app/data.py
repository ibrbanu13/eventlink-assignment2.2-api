from itertools import count

# --- Mock users ---------------------------------------------------------
# token -> user. auth.py uses this to turn "Authorization: Bearer <token>" into a user.
USERS = {                                                                             # Category                -   category
    "user-a-token": {"id": "user-a", "name": "ADA SITE", "role": "organizer"},        # ADA SITE                -   adaSite-talk ; adaSite-seminar
    "user-b-token": {"id": "user-b", "name": "ADA MUN Club", "role": "organizer"},    # ADA MUN Club            -   adaClub-mun;   
    "admin-token": {"id": "admin", "name": "Student Services", "role": "admin"},      # ADA Student Services    -   adaOffice-studentService
}

# --- Mock events --------------------------------------------------------
# id -> event. Two events organizer, one owned by the admin.
# "evt_999" is intentionally NOT here: use it to demo 404 Not Found.
_events = {
    "evt_101": {
        "id":           "evt_101",
        "title":        "Introduction to Education Program of Faculty of International Resource Sciences Akita University, Japan",
        "description":  [
                            "Akita University’s Faculty of International Resource Sciences cultivates global specialists for overseas resource development and management. ",
                            "Integrating social sciences, humanities, natural sciences, and engineering, ",
                            "it offers three interdisciplinary programs: Resource Policy and Management, Earth Resource Sciences, and Earth Resource Engineering and Environmental Sciences. ",
                            "Key educational features include English-taught lectures from the second year and mandatory third-year overseas fieldwork, equipping students with advanced technologies and international policy discernment.",
                        ],
        "category":     "adaSite-seminar",
        "location":     "B-206",
        "startsAt":     "2026-11-25T14:00:00+04:00",
        "endsAt":       "2026-11-25T15:30:00+04:00",
        "capacity":     100,
        "registrationDeadline": None,
        "ownerId":      "user-a",
        "isUpcoming":   True,
    },
    "evt_102": {
        "id":           "evt_102",
        "title":        "Cryptography: Where we are and what is the future?",
        "description":  [
                            "Today’s digital security relies on mathematical problems that would take computers billions of years to solve, ",
                            "keeping everything from online banking to private text messages secure. ",
                            "Quantum computers will be able to crack these codes using specialized algorithms. ",
                            "To prevent a major security crisis, post quantum cryptography is developed based on interesting mathematical problems with required complexity.",
                        ],
        "category":     "adaSite-talk",
        "location":     "B-203",
        "startsAt":     "2026-11-13T16:30:00+04:00",
        "endsAt":       "2026-11-13T18:00:00+04:00",
        "capacity":     100,
        "registrationDeadline": "2026-11-12T23:59:59+04:00",
        "ownerId":      "user-a",
        "isUpcoming":   False,
    },
    "evt_103": {
        "id":           "evt_103",
        "title":        "UN Emergency Room — Can You Stop the Crisis?",
        "description":  [
                            "Imagine waking up at 5 AM to a region-wide blackout. ",
                            "Phones are down, hospitals are running out of fuel, ",
                            "and governments are pointing fingers. The UN calls an emergency meeting. ",
                            "You're in the room. What happens next?\n",
                            "ADAMUN invites you to UN Emergency Room, ",
                            "an interactive crisis simulation where your decisions could prevent a disaster from escalating into war.",
                        ],
        "category":     "adaClub-mun",
        "location":     "A-202",
        "startsAt":     "2026-11-26T16:00:00+04:00",
        "endsAt":       "2026-11-26T19:00:00+04:00",
        "capacity":     100,
        "registrationDeadline": "2026-11-24T23:59:59+04:00",
        "ownerId":      "user-b",
        "isUpcoming":   True,
    },
     "evt_104": {
        "id":           "evt_104",
        "title":        "MUN Infosession: Enter the United Nations",
        "description":  [
                            "Ever wondered what it feels like to represent a country, ",
                            "negotiate international agreements, and participate in diplomatic discussions? ",
                            "Now is your chance to find out!\n",
                            "You're in the room. What happens next?\n",
                            "ADAMUN Club invites you to an interactive introductory session ",
                            "designed for students who want to discover the world of Model United Nations.",
                        ],
        "category":     "adaClub-mun",
        "location":     "B-205",
        "startsAt":     "2026-11-13T16:00:00+04:00",
        "endsAt":       "2026-11-25T17:30:00+04:00",
        "capacity":     100,
        "registrationDeadline": None,
        "ownerId":      "user-b",
        "isUpcoming":   False,
    },
    "evt_105": {
        "id":           "evt_105",
        "title":        "WE THE ARTISTS Exhibition – Artist Talk & Workshop",
        "description":  [
                            "We are pleased to invite you to join a special meeting and workshop with the artists participating in the WE THE ARTISTS exhibition, ",
                            "whose works are currently on display at the ADA Art Gallery.\n",
                            "Following the session, a welcome reception with drinks and a light buffet will be provided, ",
                            "offering an opportunity to connect with the artists and fellow students in a relaxed atmosphere.",
                        ],
        "category":     "adaOffice-studentService",
        "location":     "F-0Theatre",
        "startsAt":     "2026-11-20T14:00:00+04:00",
        "endsAt":       "2026-11-20T17:30:00+04:00",
        "capacity":     200,
        "registrationDeadline": "2026-11-19T23:59:59+04:00",
        "ownerId":      "admin",
        "isUpcoming":   False,
    },
}

# Next id number for newly created events (evt_106, evt_107, ...).
_id_counter = count(106)


# --- Users --------------------------------------------------------------
def get_user_by_token(token):
    return USERS.get(token)


# --- Events -------------------------------------------------------------
def list_events(owner_id=None):
    events = list(_events.values())
    if owner_id is not None:
        events = [e for e in events if e["ownerId"] == owner_id]
    return events


def get_event(event_id):
    return _events.get(event_id)


def find_duplicate(owner_id, title, date, location):
#   (used for the 409 Conflict case), or None
    for event in _events.values():
        if (
            event["ownerId"] == owner_id
            and event["title"].lower() == title.lower()
            and event["date"] == date
            and event["location"].lower() == location.lower()
        ):
            return event
    return None


def create_event(fields, owner_id):
    event_id = f"evt_{next(_id_counter)}"
    event = {
        "id": event_id,
        "title": fields["title"],
        "description": fields.get("description"),
        "category": fields.get("category"),
        "location": fields["location"],
        "startsAt": fields["startsAt"],
        "endsAt": fields["endsAt"],
        "capacity": fields.get("capacity"),
        "registrationDeadline": fields.get("registrationDeadline"),
        "ownerId": owner_id,
    }
    _events[event_id] = event
    return event


def update_event(event_id, fields):
    """Update an existing event with already-validated fields. Returns the
    updated event, or None if the id does not exist. id and ownerId are
    never changed."""
    event = _events.get(event_id)
    if event is None:
        return None
    for key, value in fields.items():
        if key not in ("id", "ownerId"):
            event[key] = value
    return event


def delete_event(event_id):
#   Delete an event. Returns True if it existed, False otherwise.
    return _events.pop(event_id, None) is not None