# coding: utf-8

"""
    Grafeas API

    An API to insert and retrieve annotations on cloud artifacts.  # noqa: E501

    OpenAPI spec version: v1alpha1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from grafeas.models.docker_image_fingerprint import DockerImageFingerprint  # noqa: F401,E501
from grafeas.models.docker_image_layer import DockerImageLayer  # noqa: F401,E501


class DockerImageDerivedDetails(object):
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
        'fingerprint': 'DockerImageFingerprint',
        'distance': 'int',
        'layer_info': 'list[DockerImageLayer]',
        'base_resource_url': 'str'
    }

    attribute_map = {
        'fingerprint': 'fingerprint',
        'distance': 'distance',
        'layer_info': 'layer_info',
        'base_resource_url': 'base_resource_url'
    }

    def __init__(self, fingerprint=None, distance=None, layer_info=None, base_resource_url=None):  # noqa: E501
        """DockerImageDerivedDetails - a model defined in Swagger"""  # noqa: E501

        self._fingerprint = None
        self._distance = None
        self._layer_info = None
        self._base_resource_url = None
        self.discriminator = None

        if fingerprint is not None:
            self.fingerprint = fingerprint
        if distance is not None:
            self.distance = distance
        if layer_info is not None:
            self.layer_info = layer_info
        if base_resource_url is not None:
            self.base_resource_url = base_resource_url

    @property
    def fingerprint(self):
        """Gets the fingerprint of this DockerImageDerivedDetails.  # noqa: E501


        :return: The fingerprint of this DockerImageDerivedDetails.  # noqa: E501
        :rtype: DockerImageFingerprint
        """
        return self._fingerprint

    @fingerprint.setter
    def fingerprint(self, fingerprint):
        """Sets the fingerprint of this DockerImageDerivedDetails.


        :param fingerprint: The fingerprint of this DockerImageDerivedDetails.  # noqa: E501
        :type: DockerImageFingerprint
        """

        self._fingerprint = fingerprint

    @property
    def distance(self):
        """Gets the distance of this DockerImageDerivedDetails.  # noqa: E501

        Output only. The number of layers by which this image differs from the associated image basis.  # noqa: E501

        :return: The distance of this DockerImageDerivedDetails.  # noqa: E501
        :rtype: int
        """
        return self._distance

    @distance.setter
    def distance(self, distance):
        """Sets the distance of this DockerImageDerivedDetails.

        Output only. The number of layers by which this image differs from the associated image basis.  # noqa: E501

        :param distance: The distance of this DockerImageDerivedDetails.  # noqa: E501
        :type: int
        """

        self._distance = distance

    @property
    def layer_info(self):
        """Gets the layer_info of this DockerImageDerivedDetails.  # noqa: E501

        This contains layer-specific metadata, if populated it has length \"distance\" and is ordered with [distance] being the layer immediately following the base image and [1] being the final layer.  # noqa: E501

        :return: The layer_info of this DockerImageDerivedDetails.  # noqa: E501
        :rtype: list[DockerImageLayer]
        """
        return self._layer_info

    @layer_info.setter
    def layer_info(self, layer_info):
        """Sets the layer_info of this DockerImageDerivedDetails.

        This contains layer-specific metadata, if populated it has length \"distance\" and is ordered with [distance] being the layer immediately following the base image and [1] being the final layer.  # noqa: E501

        :param layer_info: The layer_info of this DockerImageDerivedDetails.  # noqa: E501
        :type: list[DockerImageLayer]
        """

        self._layer_info = layer_info

    @property
    def base_resource_url(self):
        """Gets the base_resource_url of this DockerImageDerivedDetails.  # noqa: E501


        :return: The base_resource_url of this DockerImageDerivedDetails.  # noqa: E501
        :rtype: str
        """
        return self._base_resource_url

    @base_resource_url.setter
    def base_resource_url(self, base_resource_url):
        """Sets the base_resource_url of this DockerImageDerivedDetails.


        :param base_resource_url: The base_resource_url of this DockerImageDerivedDetails.  # noqa: E501
        :type: str
        """

        self._base_resource_url = base_resource_url

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DockerImageDerivedDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
