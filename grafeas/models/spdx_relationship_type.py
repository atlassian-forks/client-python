# coding: utf-8

"""
    grafeas.proto

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: version not set
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SpdxRelationshipType(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    RELATIONSHIP_TYPE_UNSPECIFIED = "RELATIONSHIP_TYPE_UNSPECIFIED"
    DESCRIBES = "DESCRIBES"
    DESCRIBED_BY = "DESCRIBED_BY"
    CONTAINS = "CONTAINS"
    CONTAINED_BY = "CONTAINED_BY"
    DEPENDS_ON = "DEPENDS_ON"
    DEPENDENCY_OF = "DEPENDENCY_OF"
    DEPENDENCY_MANIFEST_OF = "DEPENDENCY_MANIFEST_OF"
    BUILD_DEPENDENCY_OF = "BUILD_DEPENDENCY_OF"
    DEV_DEPENDENCY_OF = "DEV_DEPENDENCY_OF"
    OPTIONAL_DEPENDENCY_OF = "OPTIONAL_DEPENDENCY_OF"
    PROVIDED_DEPENDENCY_OF = "PROVIDED_DEPENDENCY_OF"
    TEST_DEPENDENCY_OF = "TEST_DEPENDENCY_OF"
    RUNTIME_DEPENDENCY_OF = "RUNTIME_DEPENDENCY_OF"
    EXAMPLE_OF = "EXAMPLE_OF"
    GENERATES = "GENERATES"
    GENERATED_FROM = "GENERATED_FROM"
    ANCESTOR_OF = "ANCESTOR_OF"
    DESCENDANT_OF = "DESCENDANT_OF"
    VARIANT_OF = "VARIANT_OF"
    DISTRIBUTION_ARTIFACT = "DISTRIBUTION_ARTIFACT"
    PATCH_FOR = "PATCH_FOR"
    PATCH_APPLIED = "PATCH_APPLIED"
    COPY_OF = "COPY_OF"
    FILE_ADDED = "FILE_ADDED"
    FILE_DELETED = "FILE_DELETED"
    FILE_MODIFIED = "FILE_MODIFIED"
    EXPANDED_FROM_ARCHIVE = "EXPANDED_FROM_ARCHIVE"
    DYNAMIC_LINK = "DYNAMIC_LINK"
    STATIC_LINK = "STATIC_LINK"
    DATA_FILE_OF = "DATA_FILE_OF"
    TEST_CASE_OF = "TEST_CASE_OF"
    BUILD_TOOL_OF = "BUILD_TOOL_OF"
    DEV_TOOL_OF = "DEV_TOOL_OF"
    TEST_OF = "TEST_OF"
    TEST_TOOL_OF = "TEST_TOOL_OF"
    DOCUMENTATION_OF = "DOCUMENTATION_OF"
    OPTIONAL_COMPONENT_OF = "OPTIONAL_COMPONENT_OF"
    METAFILE_OF = "METAFILE_OF"
    PACKAGE_OF = "PACKAGE_OF"
    AMENDS = "AMENDS"
    PREREQUISITE_FOR = "PREREQUISITE_FOR"
    HAS_PREREQUISITE = "HAS_PREREQUISITE"
    OTHER = "OTHER"

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
    }

    attribute_map = {
    }

    def __init__(self):  # noqa: E501
        """SpdxRelationshipType - a model defined in Swagger"""  # noqa: E501
        self.discriminator = None

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(SpdxRelationshipType, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SpdxRelationshipType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other