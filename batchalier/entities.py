"""Module that holds common entities to be used by both submitter/processor"""
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Any, Optional
from uuid import UUID, uuid4


class JobStatus(Enum):
    """
    Current status of the job:
        NEW: Job has been created but not yet submitted
        QUEUED: Job has been submitted to a JobSubmitter, batching before sending to the bus.
        SUBMITTED: The Job has been sent to the bus.
        FAILED: A fatal error has occured and the Job could not be submitted to the bus.
    """

    NEW = auto()
    QUEUED = auto()
    SUBMITTED = auto()
    FAILED = auto()


class ResultCode(Enum):
    """
    The result of the job:
        PROCESSED_OK: Job has been processed successfully.
        PROCESSED_ERROR: Job was accepted for processing but resulted in some kind of error.
    """

    PROCESSED_OK = 0
    PROCESSED_ERROR = 1


class Priority(Enum):
    """
    Priority of the job/result. Controls batching config and processing order for the job.
      REALTIME: Highest priority class. Do not batch; send immediately.
      NORMAL: Arbitrary identifier for the type of job so processor knows how to read the data.
      SLOW: The result of the job; it will be processed (OK||ERROR) or failed.
    """

    REALTIME = auto()
    NORMAL = auto()
    SLOW = auto()


@dataclass
class Job:
    """
    A unit of work submitted to Batchalier for batched streaming to a processor.
      processor: Arbitrary identifier for the job processor application e.g. payments
      group: Arbitrary identifier for the type of job so processor knows how to read the data.
      priority: The priority class of the job.
      status: Current status of the job.
      data: Arbitrary data. A processor must know the group to interpret the job data.
      queued_at: Timestamp (epoch seconds) when the job was submitted for batching.
      submitted_at: Timestamp (epoch seconds) when the job batch was sent to the bus.
    """

    # pylint: disable=too-many-instance-attributes
    _id: UUID = field(default_factory=uuid4)
    processor: str = ""
    group: str = ""
    priority: Optional[Priority] = None
    status: Optional[JobStatus] = None
    data: Any = None
    queued_at: float = -1
    submitted_at: float = -1


@dataclass
class JobResult:
    """
    The proessed result from a job.
      job_id: ID of the job which this result is for.
      job_group: Arbitrary identifier for the type of job so processor knows how to read the data.
      priority: The priority class of the job result. Will match the job.
      result: The result of the job; it will be processed (OK||ERROR) or failed.
      data: Arbitrary data. A submitter must interpret the result data based on the group.
      processed_at: The timestamp (epoch seconds) when the job was processed. Set by processor.
    """

    job_id: UUID = field(default_factory=uuid4)
    job_group: str = ""
    priority: Optional[Priority] = None
    result: Optional[ResultCode] = None
    data: Any = None
    processed_at: float = -1
