import localVarRequest from 'request';

export * from './accuracyInput';
export * from './apiResponse';
export * from './bucketizeInput';
export * from './bucketizeOutput';
export * from './category';
export * from './correlationInput';
export * from './correlationMatrixInput';
export * from './correlationMatrixOutput';
export * from './correlationOutput';
export * from './covarianceInput';
export * from './covarianceOutput';
export * from './dataRangeInput';
export * from './dataRangeOutput';
export * from './deMeanInput';
export * from './deMeanOutput';
export * from './differenceQuotientInput';
export * from './differenceQuotientOutput';
export * from './distanceInput';
export * from './distanceOutput';
export * from './dotInput';
export * from './dotOutput';
export * from './estimateGradientInput';
export * from './estimateGradientOutput';
export * from './f1ScoreInput';
export * from './getColumnInput';
export * from './getColumnOutput';
export * from './getRowInput';
export * from './getRowOutput';
export * from './inRandomOrderInput';
export * from './interquartileRangeInput';
export * from './magnitudeInput';
export * from './matrixAddInput';
export * from './maximizeBatchInput';
export * from './maximizeBatchOutput';
export * from './maximizeStochasticInput';
export * from './maximizeStochasticOutput';
export * from './meanInput';
export * from './medianInput';
export * from './minimizeBatchInput';
export * from './minimizeBatchOutput';
export * from './minimizeStochasticInput';
export * from './minimizeStochasticOutput';
export * from './modeInput';
export * from './order';
export * from './partialDifferenceQuotientInput';
export * from './partialDifferenceQuotientOutput';
export * from './pet';
export * from './precisionInput';
export * from './quantileInput';
export * from './recallInput';
export * from './scalarMultiplyInput';
export * from './shapeInput';
export * from './shapeOutput';
export * from './splitDataInput';
export * from './splitDataOutput';
export * from './sqrtInput';
export * from './sqrtOutput';
export * from './squaredDistanceInput';
export * from './standardDeviationInput';
export * from './strengthInput';
export * from './strengthOutput';
export * from './sumOfSquaresInput';
export * from './tag';
export * from './trainTestSplitInput';
export * from './trainTestSplitOutput';
export * from './user';
export * from './varianceInput';
export * from './vectorAddInput';
export * from './vectorMeanInput';
export * from './vectorSubtractInput';
export * from './vectorSumInput';

import * as fs from 'fs';

export interface RequestDetailedFile {
    value: Buffer;
    options?: {
        filename?: string;
        contentType?: string;
    }
}

export type RequestFile = string | Buffer | fs.ReadStream | RequestDetailedFile;


import { AccuracyInput } from './accuracyInput';
import { ApiResponse } from './apiResponse';
import { BucketizeInput } from './bucketizeInput';
import { BucketizeOutput } from './bucketizeOutput';
import { Category } from './category';
import { CorrelationInput } from './correlationInput';
import { CorrelationMatrixInput } from './correlationMatrixInput';
import { CorrelationMatrixOutput } from './correlationMatrixOutput';
import { CorrelationOutput } from './correlationOutput';
import { CovarianceInput } from './covarianceInput';
import { CovarianceOutput } from './covarianceOutput';
import { DataRangeInput } from './dataRangeInput';
import { DataRangeOutput } from './dataRangeOutput';
import { DeMeanInput } from './deMeanInput';
import { DeMeanOutput } from './deMeanOutput';
import { DifferenceQuotientInput } from './differenceQuotientInput';
import { DifferenceQuotientOutput } from './differenceQuotientOutput';
import { DistanceInput } from './distanceInput';
import { DistanceOutput } from './distanceOutput';
import { DotInput } from './dotInput';
import { DotOutput } from './dotOutput';
import { EstimateGradientInput } from './estimateGradientInput';
import { EstimateGradientOutput } from './estimateGradientOutput';
import { F1ScoreInput } from './f1ScoreInput';
import { GetColumnInput } from './getColumnInput';
import { GetColumnOutput } from './getColumnOutput';
import { GetRowInput } from './getRowInput';
import { GetRowOutput } from './getRowOutput';
import { InRandomOrderInput } from './inRandomOrderInput';
import { InterquartileRangeInput } from './interquartileRangeInput';
import { MagnitudeInput } from './magnitudeInput';
import { MatrixAddInput } from './matrixAddInput';
import { MaximizeBatchInput } from './maximizeBatchInput';
import { MaximizeBatchOutput } from './maximizeBatchOutput';
import { MaximizeStochasticInput } from './maximizeStochasticInput';
import { MaximizeStochasticOutput } from './maximizeStochasticOutput';
import { MeanInput } from './meanInput';
import { MedianInput } from './medianInput';
import { MinimizeBatchInput } from './minimizeBatchInput';
import { MinimizeBatchOutput } from './minimizeBatchOutput';
import { MinimizeStochasticInput } from './minimizeStochasticInput';
import { MinimizeStochasticOutput } from './minimizeStochasticOutput';
import { ModeInput } from './modeInput';
import { Order } from './order';
import { PartialDifferenceQuotientInput } from './partialDifferenceQuotientInput';
import { PartialDifferenceQuotientOutput } from './partialDifferenceQuotientOutput';
import { Pet } from './pet';
import { PrecisionInput } from './precisionInput';
import { QuantileInput } from './quantileInput';
import { RecallInput } from './recallInput';
import { ScalarMultiplyInput } from './scalarMultiplyInput';
import { ShapeInput } from './shapeInput';
import { ShapeOutput } from './shapeOutput';
import { SplitDataInput } from './splitDataInput';
import { SplitDataOutput } from './splitDataOutput';
import { SqrtInput } from './sqrtInput';
import { SqrtOutput } from './sqrtOutput';
import { SquaredDistanceInput } from './squaredDistanceInput';
import { StandardDeviationInput } from './standardDeviationInput';
import { StrengthInput } from './strengthInput';
import { StrengthOutput } from './strengthOutput';
import { SumOfSquaresInput } from './sumOfSquaresInput';
import { Tag } from './tag';
import { TrainTestSplitInput } from './trainTestSplitInput';
import { TrainTestSplitOutput } from './trainTestSplitOutput';
import { User } from './user';
import { VarianceInput } from './varianceInput';
import { VectorAddInput } from './vectorAddInput';
import { VectorMeanInput } from './vectorMeanInput';
import { VectorSubtractInput } from './vectorSubtractInput';
import { VectorSumInput } from './vectorSumInput';

/* tslint:disable:no-unused-variable */
let primitives = [
                    "string",
                    "boolean",
                    "double",
                    "integer",
                    "long",
                    "float",
                    "number",
                    "any"
                 ];

let enumsMap: {[index: string]: any} = {
        "Order.StatusEnum": Order.StatusEnum,
        "Pet.StatusEnum": Pet.StatusEnum,
}

let typeMap: {[index: string]: any} = {
    "AccuracyInput": AccuracyInput,
    "ApiResponse": ApiResponse,
    "BucketizeInput": BucketizeInput,
    "BucketizeOutput": BucketizeOutput,
    "Category": Category,
    "CorrelationInput": CorrelationInput,
    "CorrelationMatrixInput": CorrelationMatrixInput,
    "CorrelationMatrixOutput": CorrelationMatrixOutput,
    "CorrelationOutput": CorrelationOutput,
    "CovarianceInput": CovarianceInput,
    "CovarianceOutput": CovarianceOutput,
    "DataRangeInput": DataRangeInput,
    "DataRangeOutput": DataRangeOutput,
    "DeMeanInput": DeMeanInput,
    "DeMeanOutput": DeMeanOutput,
    "DifferenceQuotientInput": DifferenceQuotientInput,
    "DifferenceQuotientOutput": DifferenceQuotientOutput,
    "DistanceInput": DistanceInput,
    "DistanceOutput": DistanceOutput,
    "DotInput": DotInput,
    "DotOutput": DotOutput,
    "EstimateGradientInput": EstimateGradientInput,
    "EstimateGradientOutput": EstimateGradientOutput,
    "F1ScoreInput": F1ScoreInput,
    "GetColumnInput": GetColumnInput,
    "GetColumnOutput": GetColumnOutput,
    "GetRowInput": GetRowInput,
    "GetRowOutput": GetRowOutput,
    "InRandomOrderInput": InRandomOrderInput,
    "InterquartileRangeInput": InterquartileRangeInput,
    "MagnitudeInput": MagnitudeInput,
    "MatrixAddInput": MatrixAddInput,
    "MaximizeBatchInput": MaximizeBatchInput,
    "MaximizeBatchOutput": MaximizeBatchOutput,
    "MaximizeStochasticInput": MaximizeStochasticInput,
    "MaximizeStochasticOutput": MaximizeStochasticOutput,
    "MeanInput": MeanInput,
    "MedianInput": MedianInput,
    "MinimizeBatchInput": MinimizeBatchInput,
    "MinimizeBatchOutput": MinimizeBatchOutput,
    "MinimizeStochasticInput": MinimizeStochasticInput,
    "MinimizeStochasticOutput": MinimizeStochasticOutput,
    "ModeInput": ModeInput,
    "Order": Order,
    "PartialDifferenceQuotientInput": PartialDifferenceQuotientInput,
    "PartialDifferenceQuotientOutput": PartialDifferenceQuotientOutput,
    "Pet": Pet,
    "PrecisionInput": PrecisionInput,
    "QuantileInput": QuantileInput,
    "RecallInput": RecallInput,
    "ScalarMultiplyInput": ScalarMultiplyInput,
    "ShapeInput": ShapeInput,
    "ShapeOutput": ShapeOutput,
    "SplitDataInput": SplitDataInput,
    "SplitDataOutput": SplitDataOutput,
    "SqrtInput": SqrtInput,
    "SqrtOutput": SqrtOutput,
    "SquaredDistanceInput": SquaredDistanceInput,
    "StandardDeviationInput": StandardDeviationInput,
    "StrengthInput": StrengthInput,
    "StrengthOutput": StrengthOutput,
    "SumOfSquaresInput": SumOfSquaresInput,
    "Tag": Tag,
    "TrainTestSplitInput": TrainTestSplitInput,
    "TrainTestSplitOutput": TrainTestSplitOutput,
    "User": User,
    "VarianceInput": VarianceInput,
    "VectorAddInput": VectorAddInput,
    "VectorMeanInput": VectorMeanInput,
    "VectorSubtractInput": VectorSubtractInput,
    "VectorSumInput": VectorSumInput,
}

export class ObjectSerializer {
    public static findCorrectType(data: any, expectedType: string) {
        if (data == undefined) {
            return expectedType;
        } else if (primitives.indexOf(expectedType.toLowerCase()) !== -1) {
            return expectedType;
        } else if (expectedType === "Date") {
            return expectedType;
        } else {
            if (enumsMap[expectedType]) {
                return expectedType;
            }

            if (!typeMap[expectedType]) {
                return expectedType; // w/e we don't know the type
            }

            // Check the discriminator
            let discriminatorProperty = typeMap[expectedType].discriminator;
            if (discriminatorProperty == null) {
                return expectedType; // the type does not have a discriminator. use it.
            } else {
                if (data[discriminatorProperty]) {
                    var discriminatorType = data[discriminatorProperty];
                    if(typeMap[discriminatorType]){
                        return discriminatorType; // use the type given in the discriminator
                    } else {
                        return expectedType; // discriminator did not map to a type
                    }
                } else {
                    return expectedType; // discriminator was not present (or an empty string)
                }
            }
        }
    }

    public static serialize(data: any, type: string) {
        if (data == undefined) {
            return data;
        } else if (primitives.indexOf(type.toLowerCase()) !== -1) {
            return data;
        } else if (type.lastIndexOf("Array<", 0) === 0) { // string.startsWith pre es6
            let subType: string = type.replace("Array<", ""); // Array<Type> => Type>
            subType = subType.substring(0, subType.length - 1); // Type> => Type
            let transformedData: any[] = [];
            for (let index = 0; index < data.length; index++) {
                let datum = data[index];
                transformedData.push(ObjectSerializer.serialize(datum, subType));
            }
            return transformedData;
        } else if (type === "Date") {
            return data.toISOString();
        } else {
            if (enumsMap[type]) {
                return data;
            }
            if (!typeMap[type]) { // in case we dont know the type
                return data;
            }

            // Get the actual type of this object
            type = this.findCorrectType(data, type);

            // get the map for the correct type.
            let attributeTypes = typeMap[type].getAttributeTypeMap();
            let instance: {[index: string]: any} = {};
            for (let index = 0; index < attributeTypes.length; index++) {
                let attributeType = attributeTypes[index];
                instance[attributeType.baseName] = ObjectSerializer.serialize(data[attributeType.name], attributeType.type);
            }
            return instance;
        }
    }

    public static deserialize(data: any, type: string) {
        // polymorphism may change the actual type.
        type = ObjectSerializer.findCorrectType(data, type);
        if (data == undefined) {
            return data;
        } else if (primitives.indexOf(type.toLowerCase()) !== -1) {
            return data;
        } else if (type.lastIndexOf("Array<", 0) === 0) { // string.startsWith pre es6
            let subType: string = type.replace("Array<", ""); // Array<Type> => Type>
            subType = subType.substring(0, subType.length - 1); // Type> => Type
            let transformedData: any[] = [];
            for (let index = 0; index < data.length; index++) {
                let datum = data[index];
                transformedData.push(ObjectSerializer.deserialize(datum, subType));
            }
            return transformedData;
        } else if (type === "Date") {
            return new Date(data);
        } else {
            if (enumsMap[type]) {// is Enum
                return data;
            }

            if (!typeMap[type]) { // dont know the type
                return data;
            }
            let instance = new typeMap[type]();
            let attributeTypes = typeMap[type].getAttributeTypeMap();
            for (let index = 0; index < attributeTypes.length; index++) {
                let attributeType = attributeTypes[index];
                instance[attributeType.name] = ObjectSerializer.deserialize(data[attributeType.baseName], attributeType.type);
            }
            return instance;
        }
    }
}

export interface Authentication {
    /**
    * Apply authentication settings to header and query params.
    */
    applyToRequest(requestOptions: localVarRequest.Options): Promise<void> | void;
}

export class HttpBasicAuth implements Authentication {
    public username: string = '';
    public password: string = '';

    applyToRequest(requestOptions: localVarRequest.Options): void {
        requestOptions.auth = {
            username: this.username, password: this.password
        }
    }
}

export class HttpBearerAuth implements Authentication {
    public accessToken: string | (() => string) = '';

    applyToRequest(requestOptions: localVarRequest.Options): void {
        if (requestOptions && requestOptions.headers) {
            const accessToken = typeof this.accessToken === 'function'
                            ? this.accessToken()
                            : this.accessToken;
            requestOptions.headers["Authorization"] = "Bearer " + accessToken;
        }
    }
}

export class ApiKeyAuth implements Authentication {
    public apiKey: string = '';

    constructor(private location: string, private paramName: string) {
    }

    applyToRequest(requestOptions: localVarRequest.Options): void {
        if (this.location == "query") {
            (<any>requestOptions.qs)[this.paramName] = this.apiKey;
        } else if (this.location == "header" && requestOptions && requestOptions.headers) {
            requestOptions.headers[this.paramName] = this.apiKey;
        } else if (this.location == 'cookie' && requestOptions && requestOptions.headers) {
            if (requestOptions.headers['Cookie']) {
                requestOptions.headers['Cookie'] += '; ' + this.paramName + '=' + encodeURIComponent(this.apiKey);
            }
            else {
                requestOptions.headers['Cookie'] = this.paramName + '=' + encodeURIComponent(this.apiKey);
            }
        }
    }
}

export class OAuth implements Authentication {
    public accessToken: string = '';

    applyToRequest(requestOptions: localVarRequest.Options): void {
        if (requestOptions && requestOptions.headers) {
            requestOptions.headers["Authorization"] = "Bearer " + this.accessToken;
        }
    }
}

export class VoidAuth implements Authentication {
    public username: string = '';
    public password: string = '';

    applyToRequest(_: localVarRequest.Options): void {
        // Do nothing
    }
}

export type Interceptor = (requestOptions: localVarRequest.Options) => (Promise<void> | void);
