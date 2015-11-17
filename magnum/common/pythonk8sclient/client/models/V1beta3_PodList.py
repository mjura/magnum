#!/usr/bin/env python
"""
Copyright 2015 Reverb Technologies, Inc.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

class V1beta3_PodList(object):
    """NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'apiVersion': 'str',
            
            
            'items': 'list[V1beta3_Pod]',
            
            
            'kind': 'str',
            
            
            'resourceVersion': 'str',
            
            
            'selfLink': 'str'
            
        }

        self.attributeMap = {
            
            'apiVersion': 'apiVersion',
            
            'items': 'items',
            
            'kind': 'kind',
            
            'resourceVersion': 'resourceVersion',
            
            'selfLink': 'selfLink'
            
        }       

        
        #version of the schema the object should have
        
        self.apiVersion = None # str
        
        #list of pods
        
        self.items = None # list[V1beta3_Pod]
        
        #kind of object, in CamelCase; cannot be updated
        
        self.kind = None # str
        
        #string that identifies the internal version of this object that can be used by clients to determine when objects have changed; populated by the system, read-only; value must be treated as opaque by clients and passed unmodified back to the server: https://github.com/GoogleCloudPlatform/kubernetes/blob/master/docs/api-conventions.md#concurrency-control-and-consistency
        
        self.resourceVersion = None # str
        
        #URL for the object; populated by the system, read-only
        
        self.selfLink = None # str
        