/**
 * Swagger Petstore
 * This is a sample server Petstore server.  You can find out more about     Swagger at [http://swagger.io](http://swagger.io) or on [irc.freenode.net, #swagger](http://swagger.io/irc/).      For this sample, you can use the api key `special-key` to test the authorization     filters.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: apiteam@swagger.io
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { RequestFile } from './models';

export class SplitDataOutput {
    'train'?: Array<Array<number>>;
    'test'?: Array<Array<number>>;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "train",
            "baseName": "train",
            "type": "Array<Array<number>>"
        },
        {
            "name": "test",
            "baseName": "test",
            "type": "Array<Array<number>>"
        }    ];

    static getAttributeTypeMap() {
        return SplitDataOutput.attributeTypeMap;
    }
}

