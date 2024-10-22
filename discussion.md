# Discussion

Open thinking about the ideal `log` thing.






## Shower feats & caveats


### atomic history

#### atomic rollback

> **Case to solve**  
> *"I want to undo this old command from my system, but keep everything else that happened since."*

`log` should let you rollback any command from wherever in history.  
If you did `touch this`, then it should `rm /home/$USER/this.file` to undo it.  
If you did `chmod 666 …`, then it should `chmod 644` (or whatever was the previous mode).

This implies a reverse method to undo all changes, probably in reverse order. If `log` indeed knows everything that happened (by storing `stdout` and `stdlog` at all times), it can rollback simple commands, and with LLMs we can even deduce back a lot of hidden behaviors that might not have been apparent.

Snapshots can help too in that regard, if we can `diff` with the n-1 of the concerned command, to see what really happened to which files, and then use this delta to undo it without affecting later changes that might be kept. It's tricky sometimes: it should delete a line that was created by the concerned command, even if that line had edits; however a line that was simply edited at the time, and that edit later rewritten with another thing, should remain as it is. Hopefully, AI can bridge that gap in many cases, and we can offer a review diff of changes prior to execution.


