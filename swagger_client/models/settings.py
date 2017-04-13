# coding: utf-8

"""
    Veritas Information Classifier (VIC)

    APIs

    OpenAPI spec version: Resource Specific
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Settings(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, admin_port=None, policy_management_enabled=None, classification_enabled=None, max_classify_document_size_bytes=None, max_concurrent_classify_requests=None):
        """
        Settings - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'admin_port': 'int',
            'policy_management_enabled': 'bool',
            'classification_enabled': 'bool',
            'max_classify_document_size_bytes': 'int',
            'max_concurrent_classify_requests': 'int'
        }

        self.attribute_map = {
            'admin_port': 'adminPort',
            'policy_management_enabled': 'policyManagementEnabled',
            'classification_enabled': 'classificationEnabled',
            'max_classify_document_size_bytes': 'maxClassifyDocumentSizeBytes',
            'max_concurrent_classify_requests': 'maxConcurrentClassifyRequests'
        }

        self._admin_port = admin_port
        self._policy_management_enabled = policy_management_enabled
        self._classification_enabled = classification_enabled
        self._max_classify_document_size_bytes = max_classify_document_size_bytes
        self._max_concurrent_classify_requests = max_concurrent_classify_requests

    @property
    def admin_port(self):
        """
        Gets the admin_port of this Settings.

        :return: The admin_port of this Settings.
        :rtype: int
        """
        return self._admin_port

    @admin_port.setter
    def admin_port(self, admin_port):
        """
        Sets the admin_port of this Settings.

        :param admin_port: The admin_port of this Settings.
        :type: int
        """

        self._admin_port = admin_port

    @property
    def policy_management_enabled(self):
        """
        Gets the policy_management_enabled of this Settings.
        True if this VIC instance supports policy management operations.

        :return: The policy_management_enabled of this Settings.
        :rtype: bool
        """
        return self._policy_management_enabled

    @policy_management_enabled.setter
    def policy_management_enabled(self, policy_management_enabled):
        """
        Sets the policy_management_enabled of this Settings.
        True if this VIC instance supports policy management operations.

        :param policy_management_enabled: The policy_management_enabled of this Settings.
        :type: bool
        """

        self._policy_management_enabled = policy_management_enabled

    @property
    def classification_enabled(self):
        """
        Gets the classification_enabled of this Settings.
        True if this VIC instance supports document classification operations.

        :return: The classification_enabled of this Settings.
        :rtype: bool
        """
        return self._classification_enabled

    @classification_enabled.setter
    def classification_enabled(self, classification_enabled):
        """
        Sets the classification_enabled of this Settings.
        True if this VIC instance supports document classification operations.

        :param classification_enabled: The classification_enabled of this Settings.
        :type: bool
        """

        self._classification_enabled = classification_enabled

    @property
    def max_classify_document_size_bytes(self):
        """
        Gets the max_classify_document_size_bytes of this Settings.
        Maximum size of document that can be classified.

        :return: The max_classify_document_size_bytes of this Settings.
        :rtype: int
        """
        return self._max_classify_document_size_bytes

    @max_classify_document_size_bytes.setter
    def max_classify_document_size_bytes(self, max_classify_document_size_bytes):
        """
        Sets the max_classify_document_size_bytes of this Settings.
        Maximum size of document that can be classified.

        :param max_classify_document_size_bytes: The max_classify_document_size_bytes of this Settings.
        :type: int
        """

        self._max_classify_document_size_bytes = max_classify_document_size_bytes

    @property
    def max_concurrent_classify_requests(self):
        """
        Gets the max_concurrent_classify_requests of this Settings.
        Maximum number of classification operations that the service will process concurrently.

        :return: The max_concurrent_classify_requests of this Settings.
        :rtype: int
        """
        return self._max_concurrent_classify_requests

    @max_concurrent_classify_requests.setter
    def max_concurrent_classify_requests(self, max_concurrent_classify_requests):
        """
        Sets the max_concurrent_classify_requests of this Settings.
        Maximum number of classification operations that the service will process concurrently.

        :param max_concurrent_classify_requests: The max_concurrent_classify_requests of this Settings.
        :type: int
        """

        self._max_concurrent_classify_requests = max_concurrent_classify_requests

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Settings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
