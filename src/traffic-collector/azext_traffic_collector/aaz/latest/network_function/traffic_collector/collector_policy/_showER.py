# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


class ShowER(AAZCommand):
    """Get the details of an ExpressRoute circuit.

    :example: Get the details of an ExpressRoute circuit.
        az network express-route show -n MyCircuit -g MyResourceGroup
    """

    _aaz_info = {
        "version": "2022-01-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/expressroutecircuits/{}", "2022-01-01"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.name = AAZStrArg(
            options=["-n", "--name"],
            help="ExpressRoute circuit name.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.ExpressRouteCircuitsGet(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class ExpressRouteCircuitsGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCircuits/{circuitName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "circuitName", self.ctx.args.name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-01-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.etag = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.id = AAZStrType()
            _schema_on_200.location = AAZStrType()
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200.sku = AAZObjectType()
            _schema_on_200.tags = AAZDictType()
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.allow_classic_operations = AAZBoolType(
                serialized_name="allowClassicOperations",
            )
            properties.authorization_key = AAZStrType(
                serialized_name="authorizationKey",
            )
            properties.authorizations = AAZListType()
            properties.bandwidth_in_gbps = AAZFloatType(
                serialized_name="bandwidthInGbps",
            )
            properties.circuit_provisioning_state = AAZStrType(
                serialized_name="circuitProvisioningState",
            )
            properties.express_route_port = AAZObjectType(
                serialized_name="expressRoutePort",
            )
            _ShowHelper._build_schema_sub_resource_read(properties.express_route_port)
            properties.gateway_manager_etag = AAZStrType(
                serialized_name="gatewayManagerEtag",
            )
            properties.global_reach_enabled = AAZBoolType(
                serialized_name="globalReachEnabled",
            )
            properties.peerings = AAZListType()
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.service_key = AAZStrType(
                serialized_name="serviceKey",
            )
            properties.service_provider_notes = AAZStrType(
                serialized_name="serviceProviderNotes",
            )
            properties.service_provider_properties = AAZObjectType(
                serialized_name="serviceProviderProperties",
            )
            properties.service_provider_provisioning_state = AAZStrType(
                serialized_name="serviceProviderProvisioningState",
            )
            properties.stag = AAZIntType(
                flags={"read_only": True},
            )

            authorizations = cls._schema_on_200.properties.authorizations
            authorizations.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.authorizations.Element
            _element.etag = AAZStrType(
                flags={"read_only": True},
            )
            _element.id = AAZStrType()
            _element.name = AAZStrType()
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties.authorizations.Element.properties
            properties.authorization_key = AAZStrType(
                serialized_name="authorizationKey",
            )
            properties.authorization_use_status = AAZStrType(
                serialized_name="authorizationUseStatus",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )

            peerings = cls._schema_on_200.properties.peerings
            peerings.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.peerings.Element
            _element.etag = AAZStrType(
                flags={"read_only": True},
            )
            _element.id = AAZStrType()
            _element.name = AAZStrType()
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties.peerings.Element.properties
            properties.azure_asn = AAZIntType(
                serialized_name="azureASN",
            )
            properties.connections = AAZListType()
            properties.express_route_connection = AAZObjectType(
                serialized_name="expressRouteConnection",
            )
            properties.gateway_manager_etag = AAZStrType(
                serialized_name="gatewayManagerEtag",
            )
            properties.ipv6_peering_config = AAZObjectType(
                serialized_name="ipv6PeeringConfig",
            )
            properties.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
                flags={"read_only": True},
            )
            properties.microsoft_peering_config = AAZObjectType(
                serialized_name="microsoftPeeringConfig",
            )
            _ShowHelper._build_schema_express_route_circuit_peering_config_read(properties.microsoft_peering_config)
            properties.peer_asn = AAZIntType(
                serialized_name="peerASN",
            )
            properties.peered_connections = AAZListType(
                serialized_name="peeredConnections",
                flags={"read_only": True},
            )
            properties.peering_type = AAZStrType(
                serialized_name="peeringType",
            )
            properties.primary_azure_port = AAZStrType(
                serialized_name="primaryAzurePort",
            )
            properties.primary_peer_address_prefix = AAZStrType(
                serialized_name="primaryPeerAddressPrefix",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.route_filter = AAZObjectType(
                serialized_name="routeFilter",
            )
            _ShowHelper._build_schema_sub_resource_read(properties.route_filter)
            properties.secondary_azure_port = AAZStrType(
                serialized_name="secondaryAzurePort",
            )
            properties.secondary_peer_address_prefix = AAZStrType(
                serialized_name="secondaryPeerAddressPrefix",
            )
            properties.shared_key = AAZStrType(
                serialized_name="sharedKey",
            )
            properties.state = AAZStrType()
            properties.stats = AAZObjectType()
            properties.vlan_id = AAZIntType(
                serialized_name="vlanId",
            )

            connections = cls._schema_on_200.properties.peerings.Element.properties.connections
            connections.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.peerings.Element.properties.connections.Element
            _element.etag = AAZStrType(
                flags={"read_only": True},
            )
            _element.id = AAZStrType()
            _element.name = AAZStrType()
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties.peerings.Element.properties.connections.Element.properties
            properties.address_prefix = AAZStrType(
                serialized_name="addressPrefix",
            )
            properties.authorization_key = AAZStrType(
                serialized_name="authorizationKey",
            )
            properties.circuit_connection_status = AAZStrType(
                serialized_name="circuitConnectionStatus",
                flags={"read_only": True},
            )
            properties.express_route_circuit_peering = AAZObjectType(
                serialized_name="expressRouteCircuitPeering",
            )
            _ShowHelper._build_schema_sub_resource_read(properties.express_route_circuit_peering)
            properties.ipv6_circuit_connection_config = AAZObjectType(
                serialized_name="ipv6CircuitConnectionConfig",
            )
            properties.peer_express_route_circuit_peering = AAZObjectType(
                serialized_name="peerExpressRouteCircuitPeering",
            )
            _ShowHelper._build_schema_sub_resource_read(properties.peer_express_route_circuit_peering)
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )

            ipv6_circuit_connection_config = cls._schema_on_200.properties.peerings.Element.properties.connections.Element.properties.ipv6_circuit_connection_config
            ipv6_circuit_connection_config.address_prefix = AAZStrType(
                serialized_name="addressPrefix",
            )
            ipv6_circuit_connection_config.circuit_connection_status = AAZStrType(
                serialized_name="circuitConnectionStatus",
                flags={"read_only": True},
            )

            express_route_connection = cls._schema_on_200.properties.peerings.Element.properties.express_route_connection
            express_route_connection.id = AAZStrType(
                flags={"read_only": True},
            )

            ipv6_peering_config = cls._schema_on_200.properties.peerings.Element.properties.ipv6_peering_config
            ipv6_peering_config.microsoft_peering_config = AAZObjectType(
                serialized_name="microsoftPeeringConfig",
            )
            _ShowHelper._build_schema_express_route_circuit_peering_config_read(ipv6_peering_config.microsoft_peering_config)
            ipv6_peering_config.primary_peer_address_prefix = AAZStrType(
                serialized_name="primaryPeerAddressPrefix",
            )
            ipv6_peering_config.route_filter = AAZObjectType(
                serialized_name="routeFilter",
            )
            _ShowHelper._build_schema_sub_resource_read(ipv6_peering_config.route_filter)
            ipv6_peering_config.secondary_peer_address_prefix = AAZStrType(
                serialized_name="secondaryPeerAddressPrefix",
            )
            ipv6_peering_config.state = AAZStrType()

            peered_connections = cls._schema_on_200.properties.peerings.Element.properties.peered_connections
            peered_connections.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.peerings.Element.properties.peered_connections.Element
            _element.etag = AAZStrType(
                flags={"read_only": True},
            )
            _element.id = AAZStrType()
            _element.name = AAZStrType()
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties.peerings.Element.properties.peered_connections.Element.properties
            properties.address_prefix = AAZStrType(
                serialized_name="addressPrefix",
            )
            properties.auth_resource_guid = AAZStrType(
                serialized_name="authResourceGuid",
            )
            properties.circuit_connection_status = AAZStrType(
                serialized_name="circuitConnectionStatus",
                flags={"read_only": True},
            )
            properties.connection_name = AAZStrType(
                serialized_name="connectionName",
            )
            properties.express_route_circuit_peering = AAZObjectType(
                serialized_name="expressRouteCircuitPeering",
            )
            _ShowHelper._build_schema_sub_resource_read(properties.express_route_circuit_peering)
            properties.peer_express_route_circuit_peering = AAZObjectType(
                serialized_name="peerExpressRouteCircuitPeering",
            )
            _ShowHelper._build_schema_sub_resource_read(properties.peer_express_route_circuit_peering)
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )

            stats = cls._schema_on_200.properties.peerings.Element.properties.stats
            stats.primarybytes_in = AAZIntType(
                serialized_name="primarybytesIn",
            )
            stats.primarybytes_out = AAZIntType(
                serialized_name="primarybytesOut",
            )
            stats.secondarybytes_in = AAZIntType(
                serialized_name="secondarybytesIn",
            )
            stats.secondarybytes_out = AAZIntType(
                serialized_name="secondarybytesOut",
            )

            service_provider_properties = cls._schema_on_200.properties.service_provider_properties
            service_provider_properties.bandwidth_in_mbps = AAZIntType(
                serialized_name="bandwidthInMbps",
            )
            service_provider_properties.peering_location = AAZStrType(
                serialized_name="peeringLocation",
            )
            service_provider_properties.service_provider_name = AAZStrType(
                serialized_name="serviceProviderName",
            )

            sku = cls._schema_on_200.sku
            sku.family = AAZStrType()
            sku.name = AAZStrType()
            sku.tier = AAZStrType()

            tags = cls._schema_on_200.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _ShowHelper:
    """Helper class for Show"""

    _schema_express_route_circuit_peering_config_read = None

    @classmethod
    def _build_schema_express_route_circuit_peering_config_read(cls, _schema):
        if cls._schema_express_route_circuit_peering_config_read is not None:
            _schema.advertised_communities = cls._schema_express_route_circuit_peering_config_read.advertised_communities
            _schema.advertised_public_prefixes = cls._schema_express_route_circuit_peering_config_read.advertised_public_prefixes
            _schema.advertised_public_prefixes_state = cls._schema_express_route_circuit_peering_config_read.advertised_public_prefixes_state
            _schema.customer_asn = cls._schema_express_route_circuit_peering_config_read.customer_asn
            _schema.legacy_mode = cls._schema_express_route_circuit_peering_config_read.legacy_mode
            _schema.routing_registry_name = cls._schema_express_route_circuit_peering_config_read.routing_registry_name
            return

        cls._schema_express_route_circuit_peering_config_read = _schema_express_route_circuit_peering_config_read = AAZObjectType()

        express_route_circuit_peering_config_read = _schema_express_route_circuit_peering_config_read
        express_route_circuit_peering_config_read.advertised_communities = AAZListType(
            serialized_name="advertisedCommunities",
        )
        express_route_circuit_peering_config_read.advertised_public_prefixes = AAZListType(
            serialized_name="advertisedPublicPrefixes",
        )
        express_route_circuit_peering_config_read.advertised_public_prefixes_state = AAZStrType(
            serialized_name="advertisedPublicPrefixesState",
            flags={"read_only": True},
        )
        express_route_circuit_peering_config_read.customer_asn = AAZIntType(
            serialized_name="customerASN",
        )
        express_route_circuit_peering_config_read.legacy_mode = AAZIntType(
            serialized_name="legacyMode",
        )
        express_route_circuit_peering_config_read.routing_registry_name = AAZStrType(
            serialized_name="routingRegistryName",
        )

        advertised_communities = _schema_express_route_circuit_peering_config_read.advertised_communities
        advertised_communities.Element = AAZStrType()

        advertised_public_prefixes = _schema_express_route_circuit_peering_config_read.advertised_public_prefixes
        advertised_public_prefixes.Element = AAZStrType()

        _schema.advertised_communities = cls._schema_express_route_circuit_peering_config_read.advertised_communities
        _schema.advertised_public_prefixes = cls._schema_express_route_circuit_peering_config_read.advertised_public_prefixes
        _schema.advertised_public_prefixes_state = cls._schema_express_route_circuit_peering_config_read.advertised_public_prefixes_state
        _schema.customer_asn = cls._schema_express_route_circuit_peering_config_read.customer_asn
        _schema.legacy_mode = cls._schema_express_route_circuit_peering_config_read.legacy_mode
        _schema.routing_registry_name = cls._schema_express_route_circuit_peering_config_read.routing_registry_name

    _schema_sub_resource_read = None

    @classmethod
    def _build_schema_sub_resource_read(cls, _schema):
        if cls._schema_sub_resource_read is not None:
            _schema.id = cls._schema_sub_resource_read.id
            return

        cls._schema_sub_resource_read = _schema_sub_resource_read = AAZObjectType()

        sub_resource_read = _schema_sub_resource_read
        sub_resource_read.id = AAZStrType()

        _schema.id = cls._schema_sub_resource_read.id


__all__ = ["ShowER"]
