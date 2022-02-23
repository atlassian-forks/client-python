# IntotoInToto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**step_name** | **str** | This field identifies the name of the step in the supply chain. | [optional] 
**signing_keys** | [**list[IntotoSigningKey]**](IntotoSigningKey.md) | This field contains the public keys that can be used to verify the signatures on the step metadata. | [optional] 
**expected_materials** | [**list[InTotoArtifactRule]**](InTotoArtifactRule.md) | The following fields contain in-toto artifact rules identifying the artifacts that enter this supply chain step, and exit the supply chain step, i.e. materials and products of the step. | [optional] 
**expected_products** | [**list[InTotoArtifactRule]**](InTotoArtifactRule.md) |  | [optional] 
**expected_command** | **list[str]** | This field contains the expected command used to perform the step. | [optional] 
**threshold** | **str** | This field contains a value that indicates the minimum number of keys that need to be used to sign the step&#39;s in-toto link. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


