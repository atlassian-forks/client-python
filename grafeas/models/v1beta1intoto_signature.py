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


class V1beta1intotoSignature(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'keyid': 'str',
        'sig': 'str'
    }

    attribute_map = {
        'keyid': 'keyid',
        'sig': 'sig'
    }

    def __init__(self, keyid=None, sig=None):  # noqa: E501
        """V1beta1intotoSignature - a model defined in Swagger"""  # noqa: E501

        self._keyid = None
        self._sig = None
        self.discriminator = None

        if keyid is not None:
            self.keyid = keyid
        if sig is not None:
            self.sig = sig

    @property
    def keyid(self):
        """Gets the keyid of this V1beta1intotoSignature.  # noqa: E501


        :return: The keyid of this V1beta1intotoSignature.  # noqa: E501
        :rtype: str
        """
        return self._keyid

    @keyid.setter
    def keyid(self, keyid):
        """Sets the keyid of this V1beta1intotoSignature.


        :param keyid: The keyid of this V1beta1intotoSignature.  # noqa: E501
        :type: str
        """

        self._keyid = keyid

    @property
    def sig(self):
        """Gets the sig of this V1beta1intotoSignature.  # noqa: E501


        :return: The sig of this V1beta1intotoSignature.  # noqa: E501
        :rtype: str
        """
        return self._sig

    @sig.setter
    def sig(self, sig):
        """Sets the sig of this V1beta1intotoSignature.


        :param sig: The sig of this V1beta1intotoSignature.  # noqa: E501
        :type: str
        """

        self._sig = sig

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
        if issubclass(V1beta1intotoSignature, dict):
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
        if not isinstance(other, V1beta1intotoSignature):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other