def cog_RPM(cogs):
    final_cog_pos = len(cogs) - 1
    return -(cogs[0]/cogs[-1]) if final_cog_pos % 2 != 0 else cogs[0]/cogs[-1]