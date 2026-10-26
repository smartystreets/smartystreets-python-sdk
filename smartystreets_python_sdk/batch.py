from typing import Any, Iterator

from smartystreets_python_sdk.exceptions import BatchFullError


class Batch:
    MAX_BATCH_SIZE = 100

    def __init__(self) -> None:
        self.named_lookups: dict[str, Any] = {}
        self.all_lookups: list[Any] = []
        self.current_index = 0

    def __getitem__(self, item: int) -> Any:
        return self.all_lookups[item]

    def __iter__(self) -> Iterator[Any]:
        self.current_index = 0
        return self.all_lookups.__iter__()

    def next(self) -> Any:
        if self.current_index >= self.__len__():
            raise StopIteration

        lookup = self.all_lookups[self.current_index]
        self.current_index += 1
        return lookup

    def add(self, lookup: Any) -> bool:
        """
        Adds a Lookup object to the batch. Raises an exception if the batch is already full (100 Lookups).
        """
        if self.is_full():
            raise BatchFullError('Batch size cannot exceed {}'.format(Batch.MAX_BATCH_SIZE))

        self.all_lookups.append(lookup)

        if lookup.input_id is None:
            return True

        self.named_lookups[lookup.input_id] = lookup

        return True

    def clear(self) -> None:
        self.named_lookups.clear()
        self.all_lookups = []

    def __len__(self) -> int:
        return len(self.all_lookups)

    def is_full(self) -> bool:
        return self.__len__() >= Batch.MAX_BATCH_SIZE

    def get_by_input_id(self, input_id: str) -> Any:
        return self.named_lookups[input_id]
