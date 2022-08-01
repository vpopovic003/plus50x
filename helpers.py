from flask import render_template


def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message), index=-1), code


lectures = [
    "Scratch",
    "C",
    "Arrays",
    "Algorithms",
    "Memory",
    "Data Structures",
    "Python",
    "SQL",
    "HTML, CSS, JavaScript",
    "Flask",
    "Emoji"
]

videos = [
    "4zy0z5W0-w4",
    "Na2wiHOnzXU",
    "xC3BZa1pcsY",
    "EXnHX-6voug",
    "l-dHFS_Pnzc",
    "urRlbmW5Txw",
    "k9RO-eEF9xo",
    "1YVIBFODn58",
    "lp-FwJwCqpE",
    "mlRlDFAyPtE",
    "oe-Iz0j1n6I"
]

shorts = [
    {
        "no shorts":"nothing"
    },
    {
        "Data Types":"Fc9htmvVZ9U",
        "Operators":"f1xZf4iJDWE",
        "Conditional Statements":"1wsaV5nVC7g",
        "Loops":"WgX8e_O7eG8",
        "Command Line":"BnJ013X02b8"
    },
    {
        "Functions":"n1glFqt3g38",
        "Variables and Scope":"GiFbdVGjF9I",
        "Debugging (“Step through”)":"---HbbANxDQ",
        "Debugging (“Step into”)":"tk3cl8hyfqM",
        "Arrays":"K1yC1xshF40",
        "Command Line Arguments":"AI6Ccfno6Pk"
    },
    {
        "Linear Search":"TwsgCHYmbbA",
        "Binary Search":"T98PIp4omUA",
        "Bubble Sort":"RT-hUXUWQ2I",
        "Selection Sort":"3hH8kTHFw2A",
        "Recursion":"mz6tAJMVmfM",
        "Merge Sort":"Ns7tGNbtvV4"
    },
    {
        "Hexadecimal":"u_atXp-NF6w",
        "Pointers":"XISnO2YhnsY",
        "Defining Custom Types":"96M4q0OnMfY",
        "Dynamic Memory Allocation":"xa4ugmMDhiE",
        "Call Stacks":"aCPkszeKRa4",
        "File Pointers":"bOF-SpEAYgk"
    },
    {
        "Data Structures":"3uGchQbk7g8",
        "Singly Linked Lists":"zQI3FyWm144",
        "Doubly Linked Lists":"FHMPswJDCvU",
        "Hash Tables":"nvzVHwrrub0",
        "Tries":"MC-iQHFdEDI"
    },
    {
        "Python":"mgBpcQRDtl0"
    },
    {
        "SQL":"AywtnUjQ6X4"
    },
    {
        "Internet Primer":"04GztBlVo_s",
        "IP":"A1g9SokDJSU",
        "TCP":"GP7uvI_6uas",
        "HTTP":"4axL8Gfw2nI",
        "HTML":"YK78KhMf7bs",
        "CSS":"Ub3FKU21ubk",
        "JavaScript":"Z93IaNfavZw",
        "DOM":"LKWJpgvfH3U"
    },
    {
        "Flask":"X0dwkDh8kwA",
        "Ajax":"dQcBs4S-wEQ"
    },
    {
        "no shorts":"nothing"
    }
]
