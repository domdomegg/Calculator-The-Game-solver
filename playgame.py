import getscreenshotsofbuttons
import buttonscreenshotanalyser
import solve
print(buttonscreenshotanalyser.data)
buttonscreenshotanalyser.data["buttonfuncs"] = solve.buttonstofuncs(buttonscreenshotanalyser.data["buttons"])

print(buttonscreenshotanalyser.data)

solve.solve(buttonscreenshotanalyser.data)