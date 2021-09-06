from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Audit")


@attr.s(auto_attribs=True)
class Audit:
    """ """

    id: Union[Unset, int] = UNSET
    actor: Union[Unset, str] = UNSET
    actee: Union[Unset, None, str] = UNSET
    action: Union[Unset, str] = UNSET
    value: Union[Unset, None, str] = UNSET
    time: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        actor = self.actor
        actee = self.actee
        action = self.action
        value = self.value
        time = self.time

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if actor is not UNSET:
            field_dict["actor"] = actor
        if actee is not UNSET:
            field_dict["actee"] = actee
        if action is not UNSET:
            field_dict["action"] = action
        if value is not UNSET:
            field_dict["value"] = value
        if time is not UNSET:
            field_dict["time"] = time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        actor = d.pop("actor", UNSET)

        actee = d.pop("actee", UNSET)

        action = d.pop("action", UNSET)

        value = d.pop("value", UNSET)

        time = d.pop("time", UNSET)

        audit = cls(
            id=id,
            actor=actor,
            actee=actee,
            action=action,
            value=value,
            time=time,
        )

        audit.additional_properties = d
        return audit

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
