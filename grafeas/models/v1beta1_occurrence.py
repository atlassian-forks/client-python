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


class V1beta1Occurrence(object):
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
        'name': 'str',
        'resource': 'V1beta1Resource',
        'note_name': 'str',
        'kind': 'V1beta1NoteKind',
        'remediation': 'str',
        'create_time': 'datetime',
        'update_time': 'datetime',
        'vulnerability': 'V1beta1vulnerabilityDetails',
        'build': 'V1beta1buildDetails',
        'derived_image': 'V1beta1imageDetails',
        'installation': 'V1beta1packageDetails',
        'deployment': 'V1beta1deploymentDetails',
        'discovered': 'V1beta1discoveryDetails',
        'attestation': 'V1beta1attestationDetails',
        'intoto': 'V1beta1intotoDetails',
        'sbom': 'SpdxDocumentOccurrence',
        'spdx_package': 'SpdxPackageInfoOccurrence',
        'spdx_file': 'SpdxFileOccurrence',
        'spdx_relationship': 'SpdxRelationshipOccurrence',
        'envelope': 'V1beta1Envelope'
    }

    attribute_map = {
        'name': 'name',
        'resource': 'resource',
        'note_name': 'noteName',
        'kind': 'kind',
        'remediation': 'remediation',
        'create_time': 'createTime',
        'update_time': 'updateTime',
        'vulnerability': 'vulnerability',
        'build': 'build',
        'derived_image': 'derivedImage',
        'installation': 'installation',
        'deployment': 'deployment',
        'discovered': 'discovered',
        'attestation': 'attestation',
        'intoto': 'intoto',
        'sbom': 'sbom',
        'spdx_package': 'spdxPackage',
        'spdx_file': 'spdxFile',
        'spdx_relationship': 'spdxRelationship',
        'envelope': 'envelope'
    }

    def __init__(self, name=None, resource=None, note_name=None, kind=None, remediation=None, create_time=None, update_time=None, vulnerability=None, build=None, derived_image=None, installation=None, deployment=None, discovered=None, attestation=None, intoto=None, sbom=None, spdx_package=None, spdx_file=None, spdx_relationship=None, envelope=None):  # noqa: E501
        """V1beta1Occurrence - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._resource = None
        self._note_name = None
        self._kind = None
        self._remediation = None
        self._create_time = None
        self._update_time = None
        self._vulnerability = None
        self._build = None
        self._derived_image = None
        self._installation = None
        self._deployment = None
        self._discovered = None
        self._attestation = None
        self._intoto = None
        self._sbom = None
        self._spdx_package = None
        self._spdx_file = None
        self._spdx_relationship = None
        self._envelope = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if resource is not None:
            self.resource = resource
        if note_name is not None:
            self.note_name = note_name
        if kind is not None:
            self.kind = kind
        if remediation is not None:
            self.remediation = remediation
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if vulnerability is not None:
            self.vulnerability = vulnerability
        if build is not None:
            self.build = build
        if derived_image is not None:
            self.derived_image = derived_image
        if installation is not None:
            self.installation = installation
        if deployment is not None:
            self.deployment = deployment
        if discovered is not None:
            self.discovered = discovered
        if attestation is not None:
            self.attestation = attestation
        if intoto is not None:
            self.intoto = intoto
        if sbom is not None:
            self.sbom = sbom
        if spdx_package is not None:
            self.spdx_package = spdx_package
        if spdx_file is not None:
            self.spdx_file = spdx_file
        if spdx_relationship is not None:
            self.spdx_relationship = spdx_relationship
        if envelope is not None:
            self.envelope = envelope

    @property
    def name(self):
        """Gets the name of this V1beta1Occurrence.  # noqa: E501

        Output only. The name of the occurrence in the form of `projects/[PROJECT_ID]/occurrences/[OCCURRENCE_ID]`.  # noqa: E501

        :return: The name of this V1beta1Occurrence.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1beta1Occurrence.

        Output only. The name of the occurrence in the form of `projects/[PROJECT_ID]/occurrences/[OCCURRENCE_ID]`.  # noqa: E501

        :param name: The name of this V1beta1Occurrence.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def resource(self):
        """Gets the resource of this V1beta1Occurrence.  # noqa: E501

        Required. Immutable. The resource for which the occurrence applies.  # noqa: E501

        :return: The resource of this V1beta1Occurrence.  # noqa: E501
        :rtype: V1beta1Resource
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this V1beta1Occurrence.

        Required. Immutable. The resource for which the occurrence applies.  # noqa: E501

        :param resource: The resource of this V1beta1Occurrence.  # noqa: E501
        :type: V1beta1Resource
        """

        self._resource = resource

    @property
    def note_name(self):
        """Gets the note_name of this V1beta1Occurrence.  # noqa: E501

        Required. Immutable. The analysis note associated with this occurrence, in the form of `projects/[PROVIDER_ID]/notes/[NOTE_ID]`. This field can be used as a filter in list requests.  # noqa: E501

        :return: The note_name of this V1beta1Occurrence.  # noqa: E501
        :rtype: str
        """
        return self._note_name

    @note_name.setter
    def note_name(self, note_name):
        """Sets the note_name of this V1beta1Occurrence.

        Required. Immutable. The analysis note associated with this occurrence, in the form of `projects/[PROVIDER_ID]/notes/[NOTE_ID]`. This field can be used as a filter in list requests.  # noqa: E501

        :param note_name: The note_name of this V1beta1Occurrence.  # noqa: E501
        :type: str
        """

        self._note_name = note_name

    @property
    def kind(self):
        """Gets the kind of this V1beta1Occurrence.  # noqa: E501

        Output only. This explicitly denotes which of the occurrence details are specified. This field can be used as a filter in list requests.  # noqa: E501

        :return: The kind of this V1beta1Occurrence.  # noqa: E501
        :rtype: V1beta1NoteKind
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this V1beta1Occurrence.

        Output only. This explicitly denotes which of the occurrence details are specified. This field can be used as a filter in list requests.  # noqa: E501

        :param kind: The kind of this V1beta1Occurrence.  # noqa: E501
        :type: V1beta1NoteKind
        """

        self._kind = kind

    @property
    def remediation(self):
        """Gets the remediation of this V1beta1Occurrence.  # noqa: E501

        A description of actions that can be taken to remedy the note.  # noqa: E501

        :return: The remediation of this V1beta1Occurrence.  # noqa: E501
        :rtype: str
        """
        return self._remediation

    @remediation.setter
    def remediation(self, remediation):
        """Sets the remediation of this V1beta1Occurrence.

        A description of actions that can be taken to remedy the note.  # noqa: E501

        :param remediation: The remediation of this V1beta1Occurrence.  # noqa: E501
        :type: str
        """

        self._remediation = remediation

    @property
    def create_time(self):
        """Gets the create_time of this V1beta1Occurrence.  # noqa: E501

        Output only. The time this occurrence was created.  # noqa: E501

        :return: The create_time of this V1beta1Occurrence.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this V1beta1Occurrence.

        Output only. The time this occurrence was created.  # noqa: E501

        :param create_time: The create_time of this V1beta1Occurrence.  # noqa: E501
        :type: datetime
        """

        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this V1beta1Occurrence.  # noqa: E501

        Output only. The time this occurrence was last updated.  # noqa: E501

        :return: The update_time of this V1beta1Occurrence.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this V1beta1Occurrence.

        Output only. The time this occurrence was last updated.  # noqa: E501

        :param update_time: The update_time of this V1beta1Occurrence.  # noqa: E501
        :type: datetime
        """

        self._update_time = update_time

    @property
    def vulnerability(self):
        """Gets the vulnerability of this V1beta1Occurrence.  # noqa: E501

        Describes a security vulnerability.  # noqa: E501

        :return: The vulnerability of this V1beta1Occurrence.  # noqa: E501
        :rtype: V1beta1vulnerabilityDetails
        """
        return self._vulnerability

    @vulnerability.setter
    def vulnerability(self, vulnerability):
        """Sets the vulnerability of this V1beta1Occurrence.

        Describes a security vulnerability.  # noqa: E501

        :param vulnerability: The vulnerability of this V1beta1Occurrence.  # noqa: E501
        :type: V1beta1vulnerabilityDetails
        """

        self._vulnerability = vulnerability

    @property
    def build(self):
        """Gets the build of this V1beta1Occurrence.  # noqa: E501

        Describes a verifiable build.  # noqa: E501

        :return: The build of this V1beta1Occurrence.  # noqa: E501
        :rtype: V1beta1buildDetails
        """
        return self._build

    @build.setter
    def build(self, build):
        """Sets the build of this V1beta1Occurrence.

        Describes a verifiable build.  # noqa: E501

        :param build: The build of this V1beta1Occurrence.  # noqa: E501
        :type: V1beta1buildDetails
        """

        self._build = build

    @property
    def derived_image(self):
        """Gets the derived_image of this V1beta1Occurrence.  # noqa: E501

        Describes how this resource derives from the basis in the associated note.  # noqa: E501

        :return: The derived_image of this V1beta1Occurrence.  # noqa: E501
        :rtype: V1beta1imageDetails
        """
        return self._derived_image

    @derived_image.setter
    def derived_image(self, derived_image):
        """Sets the derived_image of this V1beta1Occurrence.

        Describes how this resource derives from the basis in the associated note.  # noqa: E501

        :param derived_image: The derived_image of this V1beta1Occurrence.  # noqa: E501
        :type: V1beta1imageDetails
        """

        self._derived_image = derived_image

    @property
    def installation(self):
        """Gets the installation of this V1beta1Occurrence.  # noqa: E501

        Describes the installation of a package on the linked resource.  # noqa: E501

        :return: The installation of this V1beta1Occurrence.  # noqa: E501
        :rtype: V1beta1packageDetails
        """
        return self._installation

    @installation.setter
    def installation(self, installation):
        """Sets the installation of this V1beta1Occurrence.

        Describes the installation of a package on the linked resource.  # noqa: E501

        :param installation: The installation of this V1beta1Occurrence.  # noqa: E501
        :type: V1beta1packageDetails
        """

        self._installation = installation

    @property
    def deployment(self):
        """Gets the deployment of this V1beta1Occurrence.  # noqa: E501

        Describes the deployment of an artifact on a runtime.  # noqa: E501

        :return: The deployment of this V1beta1Occurrence.  # noqa: E501
        :rtype: V1beta1deploymentDetails
        """
        return self._deployment

    @deployment.setter
    def deployment(self, deployment):
        """Sets the deployment of this V1beta1Occurrence.

        Describes the deployment of an artifact on a runtime.  # noqa: E501

        :param deployment: The deployment of this V1beta1Occurrence.  # noqa: E501
        :type: V1beta1deploymentDetails
        """

        self._deployment = deployment

    @property
    def discovered(self):
        """Gets the discovered of this V1beta1Occurrence.  # noqa: E501

        Describes when a resource was discovered.  # noqa: E501

        :return: The discovered of this V1beta1Occurrence.  # noqa: E501
        :rtype: V1beta1discoveryDetails
        """
        return self._discovered

    @discovered.setter
    def discovered(self, discovered):
        """Sets the discovered of this V1beta1Occurrence.

        Describes when a resource was discovered.  # noqa: E501

        :param discovered: The discovered of this V1beta1Occurrence.  # noqa: E501
        :type: V1beta1discoveryDetails
        """

        self._discovered = discovered

    @property
    def attestation(self):
        """Gets the attestation of this V1beta1Occurrence.  # noqa: E501

        Describes an attestation of an artifact.  # noqa: E501

        :return: The attestation of this V1beta1Occurrence.  # noqa: E501
        :rtype: V1beta1attestationDetails
        """
        return self._attestation

    @attestation.setter
    def attestation(self, attestation):
        """Sets the attestation of this V1beta1Occurrence.

        Describes an attestation of an artifact.  # noqa: E501

        :param attestation: The attestation of this V1beta1Occurrence.  # noqa: E501
        :type: V1beta1attestationDetails
        """

        self._attestation = attestation

    @property
    def intoto(self):
        """Gets the intoto of this V1beta1Occurrence.  # noqa: E501

        Describes a specific in-toto link.  # noqa: E501

        :return: The intoto of this V1beta1Occurrence.  # noqa: E501
        :rtype: V1beta1intotoDetails
        """
        return self._intoto

    @intoto.setter
    def intoto(self, intoto):
        """Sets the intoto of this V1beta1Occurrence.

        Describes a specific in-toto link.  # noqa: E501

        :param intoto: The intoto of this V1beta1Occurrence.  # noqa: E501
        :type: V1beta1intotoDetails
        """

        self._intoto = intoto

    @property
    def sbom(self):
        """Gets the sbom of this V1beta1Occurrence.  # noqa: E501

        Describes a specific software bill of materials document.  # noqa: E501

        :return: The sbom of this V1beta1Occurrence.  # noqa: E501
        :rtype: SpdxDocumentOccurrence
        """
        return self._sbom

    @sbom.setter
    def sbom(self, sbom):
        """Sets the sbom of this V1beta1Occurrence.

        Describes a specific software bill of materials document.  # noqa: E501

        :param sbom: The sbom of this V1beta1Occurrence.  # noqa: E501
        :type: SpdxDocumentOccurrence
        """

        self._sbom = sbom

    @property
    def spdx_package(self):
        """Gets the spdx_package of this V1beta1Occurrence.  # noqa: E501

        Describes a specific SPDX Package.  # noqa: E501

        :return: The spdx_package of this V1beta1Occurrence.  # noqa: E501
        :rtype: SpdxPackageInfoOccurrence
        """
        return self._spdx_package

    @spdx_package.setter
    def spdx_package(self, spdx_package):
        """Sets the spdx_package of this V1beta1Occurrence.

        Describes a specific SPDX Package.  # noqa: E501

        :param spdx_package: The spdx_package of this V1beta1Occurrence.  # noqa: E501
        :type: SpdxPackageInfoOccurrence
        """

        self._spdx_package = spdx_package

    @property
    def spdx_file(self):
        """Gets the spdx_file of this V1beta1Occurrence.  # noqa: E501

        Describes a specific SPDX File.  # noqa: E501

        :return: The spdx_file of this V1beta1Occurrence.  # noqa: E501
        :rtype: SpdxFileOccurrence
        """
        return self._spdx_file

    @spdx_file.setter
    def spdx_file(self, spdx_file):
        """Sets the spdx_file of this V1beta1Occurrence.

        Describes a specific SPDX File.  # noqa: E501

        :param spdx_file: The spdx_file of this V1beta1Occurrence.  # noqa: E501
        :type: SpdxFileOccurrence
        """

        self._spdx_file = spdx_file

    @property
    def spdx_relationship(self):
        """Gets the spdx_relationship of this V1beta1Occurrence.  # noqa: E501

        Describes a specific SPDX Relationship.  # noqa: E501

        :return: The spdx_relationship of this V1beta1Occurrence.  # noqa: E501
        :rtype: SpdxRelationshipOccurrence
        """
        return self._spdx_relationship

    @spdx_relationship.setter
    def spdx_relationship(self, spdx_relationship):
        """Sets the spdx_relationship of this V1beta1Occurrence.

        Describes a specific SPDX Relationship.  # noqa: E501

        :param spdx_relationship: The spdx_relationship of this V1beta1Occurrence.  # noqa: E501
        :type: SpdxRelationshipOccurrence
        """

        self._spdx_relationship = spdx_relationship

    @property
    def envelope(self):
        """Gets the envelope of this V1beta1Occurrence.  # noqa: E501


        :return: The envelope of this V1beta1Occurrence.  # noqa: E501
        :rtype: V1beta1Envelope
        """
        return self._envelope

    @envelope.setter
    def envelope(self, envelope):
        """Sets the envelope of this V1beta1Occurrence.


        :param envelope: The envelope of this V1beta1Occurrence.  # noqa: E501
        :type: V1beta1Envelope
        """

        self._envelope = envelope

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
        if issubclass(V1beta1Occurrence, dict):
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
        if not isinstance(other, V1beta1Occurrence):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other