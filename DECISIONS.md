Processor job delivery semantics
--------------------------------
Exactly once:
+ Simplifies things and increases performance for the processor, which no longer needs to check the status of the job itself
- Kafka by default works with at-least once delivery semantics
- From a systems point of view it is easier to reason about idempotent components
- Increases complexity of Batchalier – now needs a state tracking system and exactly-once delivery is not straightforward

Outcome: Use at-least once semantics for job delivery

Sync/async for submitter
------------------------
Sync:
+ Generally simpler to reason about as failure modes are more straightforward (IMO)
- Leaves performance on the table, egregiously so in some cases

Async:
+ Natural fit for the problem domain of firing off a job and then awaiting a result using a future/callback before proceeding
+ More performant particularly when dealing with slow network I/O
+ Python kafka library supports both sync/async
- I don’t have experience designing a well tested python library that supports both sync/async interfaces - would take significantly longer

Outcome: Synchronous for now with a view to adding async support later.


Should Kafka deal in batches or jobs
------------------------------------
Jobs:
+ Kafka producers implement their own batching features, so we could just leverage their reliable well-tested code for batching and expose the configuration levers with Batchalier
+ Kafka prefers small messages (<1MB), and with arbitrary job data full batches could get very big
- Batching is a first class feature of our library so we should have more control over how it is implemented

Outcome:
* Given the problem we are dealing with maps well onto Kafkas semantics it seems sensible to use Kafka in an idiomatic way.
* For now Batchalier is 'just' a way to set up Kafka consistently and sensibly for the purpose of batching http requests between interal systems.
We will produce jobs to our topics for now.
