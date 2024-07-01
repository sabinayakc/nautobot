"""Forms and fields for apps to use."""

from nautobot.core.forms import (
    add_blank_choice,
    AddressFieldMixin,
    BootstrapMixin,
    BulkEditForm,
    BulkRenameForm,
    ConfirmationForm,
    CSVModelForm,
    DynamicFilterForm,
    ImportForm,
    PrefixFieldMixin,
    ReturnURLForm,
    TableConfigForm,
)
from nautobot.core.forms.fields import (
    CommentField,
    CSVChoiceField,
    CSVContentTypeField,
    CSVDataField,
    CSVFileField,
    CSVModelChoiceField,
    CSVMultipleChoiceField,
    CSVMultipleContentTypeField,
    DynamicModelChoiceField,
    DynamicModelChoiceMixin,
    DynamicModelMultipleChoiceField,
    ExpandableIPAddressField,
    ExpandableNameField,
    JSONArrayFormField,
    JSONField,
    LaxURLField,
    MACAddressField,
    MultiMatchModelMultipleChoiceField,
    MultipleContentTypeField,
    MultiValueCharField,
    NullableDateField,
    NumericArrayField,
    SlugField,
    TagFilterField,
)
from nautobot.core.forms.forms import dynamic_formset_factory
from nautobot.core.forms.utils import (
    add_field_to_filter_form_class,
    expand_alphanumeric_pattern,
    expand_ipaddress_pattern,
    form_from_model,
    parse_alphanumeric_range,
    parse_numeric_range,
    restrict_form_fields,
)
from nautobot.core.forms.widgets import (
    APISelect,
    APISelectMultiple,
    BulkEditNullBooleanSelect,
    ColorSelect,
    ContentTypeSelect,
    DatePicker,
    DateTimePicker,
    MultiValueCharInput,
    SelectWithDisabled,
    SelectWithPK,
    SlugWidget,
    SmallTextarea,
    StaticSelect2,
    StaticSelect2Multiple,
    TimePicker,
)
from nautobot.extras.forms import (
    CustomFieldModelBulkEditFormMixin,
    CustomFieldModelCSVForm,
    CustomFieldModelFormMixin,
    NautobotBulkEditForm,
    NautobotModelForm,
    NoteModelBulkEditFormMixin,
    NoteModelFormMixin,
    RelationshipModelBulkEditFormMixin,
    RelationshipModelFormMixin,
    StatusModelBulkEditFormMixin,
    TagsBulkEditFormMixin,
    TagsModelFilterFormMixin,
)
from nautobot.extras.forms.base import NautobotFilterForm
from nautobot.extras.forms.forms import (
    get_git_datasource_content_choices,
    provider_choices,
    provider_choices_with_blank,
)
from nautobot.extras.forms.mixins import (
    CustomFieldModelFilterFormMixin,
    NoteFormBase,
    RelationshipModelFilterFormMixin,
    RoleModelBulkEditFormMixin,
    RoleModelFilterFormMixin,
    StatusModelFilterFormMixin,
)
from nautobot.ipam.formfields import IPAddressFormField, IPNetworkFormField

__all__ = (
    "add_blank_choice",
    "add_field_to_filter_form_class",
    "AddressFieldMixin",
    "APISelect",
    "APISelectMultiple",
    "BootstrapMixin",
    "BulkEditForm",
    "BulkEditNullBooleanSelect",
    "BulkRenameForm",
    "ColorSelect",
    "CommentField",
    "ConfirmationForm",
    "ContentTypeSelect",
    "CSVChoiceField",
    "CSVContentTypeField",
    "CSVDataField",
    "CSVFileField",
    "CSVModelChoiceField",
    "CSVModelForm",
    "CSVMultipleChoiceField",
    "CSVMultipleContentTypeField",
    "CustomFieldModelBulkEditFormMixin",
    "CustomFieldModelCSVForm",
    "CustomFieldModelFilterFormMixin",
    "CustomFieldModelFormMixin",
    "DatePicker",
    "DateTimePicker",
    "dynamic_formset_factory",
    "DynamicFilterForm",
    "DynamicModelChoiceField",
    "DynamicModelChoiceMixin",
    "DynamicModelMultipleChoiceField",
    "expand_alphanumeric_pattern",
    "expand_ipaddress_pattern",
    "ExpandableIPAddressField",
    "ExpandableNameField",
    "form_from_model",
    "get_git_datasource_content_choices",
    "ImportForm",
    "IPAddressFormField",
    "IPNetworkFormField",
    "JSONArrayFormField",
    "JSONField",
    "LaxURLField",
    "MACAddressField",
    "MultiMatchModelMultipleChoiceField",
    "MultipleContentTypeField",
    "MultiValueCharField",
    "MultiValueCharInput",
    "NautobotBulkEditForm",
    "NautobotFilterForm",
    "NautobotModelForm",
    "NoteFormBase",
    "NoteModelBulkEditFormMixin",
    "NoteModelFormMixin",
    "NullableDateField",
    "NumericArrayField",
    "parse_alphanumeric_range",
    "parse_numeric_range",
    "PrefixFieldMixin",
    "provider_choices",
    "provider_choices_with_blank",
    "RelationshipModelBulkEditFormMixin",
    "RelationshipModelFilterFormMixin",
    "RelationshipModelFormMixin",
    "restrict_form_fields",
    "ReturnURLForm",
    "RoleModelBulkEditFormMixin",
    "RoleModelFilterFormMixin",
    "SelectWithDisabled",
    "SelectWithPK",
    "SlugField",
    "SlugWidget",
    "SmallTextarea",
    "StaticSelect2",
    "StaticSelect2Multiple",
    "StatusModelBulkEditFormMixin",
    "StatusModelFilterFormMixin",
    "TableConfigForm",
    "TagFilterField",
    "TagsBulkEditFormMixin",
    "TagsModelFilterFormMixin",
    "TimePicker",
)
