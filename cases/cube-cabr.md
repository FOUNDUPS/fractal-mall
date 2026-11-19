# Case 001 · Which source supplied the displayed CABR?

The build-cube JavaScript accepts simulator events when enabled. Its CABR event handler copies mapped data into display state. Outside observation mode the progress renderer may compute a value when simulator events are off or the bridge is disconnected. A screenshot records a displayed number. Which path supplied it in a particular session remains unknown without a correlated runtime trace.

[Enablement](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/public/js/foundup-cube.js#L103) · [Handler](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/public/js/foundup-cube.js#L736) · [Fallback](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/public/js/foundup-cube.js#L4016)

Source inspected 2026-11-19 JST. Status: VERIFIED_SOURCE. Runtime: UNKNOWN. This reference case is disclosed for review and cannot serve as the blind holdout.
