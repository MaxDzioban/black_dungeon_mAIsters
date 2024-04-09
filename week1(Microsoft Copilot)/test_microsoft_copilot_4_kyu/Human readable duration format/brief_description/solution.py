def format_duration(seconds):
    if seconds == 0:
        return "now"

    # Define the units and their corresponding seconds
    units = [("year", 60*60*24*365), ("day", 60*60*24), ("hour", 60*60), ("minute", 60), ("second", 1)]
    
    # Calculate the values for each unit
    values = []
    for unit, sec in units:
        q, seconds = divmod(seconds, sec)
        if q > 0:
            values.append((q, unit))

    # Format the values into strings
    parts = []
    for value, unit in values:
        part = str(value) + " " + unit + ("s" if value > 1 else "")
        parts.append(part)

    # Join the parts into a single string
    if len(parts) > 1:
        last = parts.pop()
        return ", ".join(parts) + " and " + last
    else:
        return parts[0]
