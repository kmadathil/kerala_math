
def to_mst(f: float):
    """
    Convert float input to minutes/seconds/thirds/fourths
    """
    _r = f * 60 * 60 * 60 * 60
    minutes, _r = divmod(_r, 60*60*60*60)
    seconds, _r = divmod(_r, 60*60*60)
    thirds, _r  = divmod(_r, 60*60)
    fourths, _r = divmod(_r, 60)
    return int(minutes), int(seconds), int(thirds), int(fourths)

