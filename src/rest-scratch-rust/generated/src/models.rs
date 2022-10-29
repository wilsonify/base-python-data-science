#![allow(unused_qualifications)]

use crate::models;
#[cfg(any(feature = "client", feature = "server"))]
use crate::header;

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct AccuracyInput {
    /// number of True Positives
    #[serde(rename = "tp")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub tp: Option<f64>,

    /// number of False Positives
    #[serde(rename = "fp")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub fp: Option<f64>,

    /// number of False Negatives
    #[serde(rename = "fn")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub r#fn: Option<f64>,

    /// number of True Negatives
    #[serde(rename = "tn")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub tn: Option<f64>,

}

impl AccuracyInput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> AccuracyInput {
        AccuracyInput {
            tp: None,
            fp: None,
            r#fn: None,
            tn: None,
        }
    }
}

/// Converts the AccuracyInput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for AccuracyInput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![

            self.tp.as_ref().map(|tp| {
                vec![
                    "tp".to_string(),
                    tp.to_string(),
                ].join(",")
            }),


            self.fp.as_ref().map(|fp| {
                vec![
                    "fp".to_string(),
                    fp.to_string(),
                ].join(",")
            }),


            self.r#fn.as_ref().map(|r#fn| {
                vec![
                    "fn".to_string(),
                    r#fn.to_string(),
                ].join(",")
            }),


            self.tn.as_ref().map(|tn| {
                vec![
                    "tn".to_string(),
                    tn.to_string(),
                ].join(",")
            }),

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a AccuracyInput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for AccuracyInput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub tp: Vec<f64>,
            pub fp: Vec<f64>,
            pub r#fn: Vec<f64>,
            pub tn: Vec<f64>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing AccuracyInput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    #[allow(clippy::redundant_clone)]
                    "tp" => intermediate_rep.tp.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    #[allow(clippy::redundant_clone)]
                    "fp" => intermediate_rep.fp.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    #[allow(clippy::redundant_clone)]
                    "fn" => intermediate_rep.r#fn.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    #[allow(clippy::redundant_clone)]
                    "tn" => intermediate_rep.tn.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    _ => return std::result::Result::Err("Unexpected key while parsing AccuracyInput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(AccuracyInput {
            tp: intermediate_rep.tp.into_iter().next(),
            fp: intermediate_rep.fp.into_iter().next(),
            r#fn: intermediate_rep.r#fn.into_iter().next(),
            tn: intermediate_rep.tn.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<AccuracyInput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<AccuracyInput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<AccuracyInput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for AccuracyInput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<AccuracyInput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <AccuracyInput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into AccuracyInput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl AccuracyInput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, PartialOrd, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct AccuracyOutput(f64);

impl std::convert::From<f64> for AccuracyOutput {
    fn from(x: f64) -> Self {
        AccuracyOutput(x)
    }
}

impl std::convert::From<AccuracyOutput> for f64 {
    fn from(x: AccuracyOutput) -> Self {
        x.0
    }
}

impl std::ops::Deref for AccuracyOutput {
    type Target = f64;
    fn deref(&self) -> &f64 {
        &self.0
    }
}

impl std::ops::DerefMut for AccuracyOutput {
    fn deref_mut(&mut self) -> &mut f64 {
        &mut self.0
    }
}


impl AccuracyOutput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct ApiResponse {
    #[serde(rename = "code")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub code: Option<i32>,

    #[serde(rename = "type")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub r#type: Option<String>,

    #[serde(rename = "message")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub message: Option<String>,

}

impl ApiResponse {
    #[allow(clippy::new_without_default)]
    pub fn new() -> ApiResponse {
        ApiResponse {
            code: None,
            r#type: None,
            message: None,
        }
    }
}

/// Converts the ApiResponse value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for ApiResponse {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![

            self.code.as_ref().map(|code| {
                vec![
                    "code".to_string(),
                    code.to_string(),
                ].join(",")
            }),


            self.r#type.as_ref().map(|r#type| {
                vec![
                    "type".to_string(),
                    r#type.to_string(),
                ].join(",")
            }),


            self.message.as_ref().map(|message| {
                vec![
                    "message".to_string(),
                    message.to_string(),
                ].join(",")
            }),

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a ApiResponse value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for ApiResponse {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub code: Vec<i32>,
            pub r#type: Vec<String>,
            pub message: Vec<String>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing ApiResponse".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    #[allow(clippy::redundant_clone)]
                    "code" => intermediate_rep.code.push(<i32 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    #[allow(clippy::redundant_clone)]
                    "type" => intermediate_rep.r#type.push(<String as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    #[allow(clippy::redundant_clone)]
                    "message" => intermediate_rep.message.push(<String as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    _ => return std::result::Result::Err("Unexpected key while parsing ApiResponse".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(ApiResponse {
            code: intermediate_rep.code.into_iter().next(),
            r#type: intermediate_rep.r#type.into_iter().next(),
            message: intermediate_rep.message.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<ApiResponse> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<ApiResponse>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<ApiResponse>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for ApiResponse - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<ApiResponse> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <ApiResponse as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into ApiResponse - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl ApiResponse {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct BucketizeInput {
    #[serde(rename = "point")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub point: Option<f64>,

    #[serde(rename = "bucket_size")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub bucket_size: Option<f64>,

}

impl BucketizeInput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> BucketizeInput {
        BucketizeInput {
            point: None,
            bucket_size: None,
        }
    }
}

/// Converts the BucketizeInput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for BucketizeInput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![

            self.point.as_ref().map(|point| {
                vec![
                    "point".to_string(),
                    point.to_string(),
                ].join(",")
            }),


            self.bucket_size.as_ref().map(|bucket_size| {
                vec![
                    "bucket_size".to_string(),
                    bucket_size.to_string(),
                ].join(",")
            }),

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a BucketizeInput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for BucketizeInput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub point: Vec<f64>,
            pub bucket_size: Vec<f64>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing BucketizeInput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    #[allow(clippy::redundant_clone)]
                    "point" => intermediate_rep.point.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    #[allow(clippy::redundant_clone)]
                    "bucket_size" => intermediate_rep.bucket_size.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    _ => return std::result::Result::Err("Unexpected key while parsing BucketizeInput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(BucketizeInput {
            point: intermediate_rep.point.into_iter().next(),
            bucket_size: intermediate_rep.bucket_size.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<BucketizeInput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<BucketizeInput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<BucketizeInput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for BucketizeInput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<BucketizeInput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <BucketizeInput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into BucketizeInput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl BucketizeInput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct BucketizeOutput {
    #[serde(rename = "x")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub x: Option<f64>,

    #[serde(rename = "result")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub result: Option<f64>,

}

impl BucketizeOutput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> BucketizeOutput {
        BucketizeOutput {
            x: None,
            result: None,
        }
    }
}

/// Converts the BucketizeOutput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for BucketizeOutput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![

            self.x.as_ref().map(|x| {
                vec![
                    "x".to_string(),
                    x.to_string(),
                ].join(",")
            }),


            self.result.as_ref().map(|result| {
                vec![
                    "result".to_string(),
                    result.to_string(),
                ].join(",")
            }),

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a BucketizeOutput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for BucketizeOutput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub x: Vec<f64>,
            pub result: Vec<f64>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing BucketizeOutput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    #[allow(clippy::redundant_clone)]
                    "x" => intermediate_rep.x.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    #[allow(clippy::redundant_clone)]
                    "result" => intermediate_rep.result.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    _ => return std::result::Result::Err("Unexpected key while parsing BucketizeOutput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(BucketizeOutput {
            x: intermediate_rep.x.into_iter().next(),
            result: intermediate_rep.result.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<BucketizeOutput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<BucketizeOutput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<BucketizeOutput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for BucketizeOutput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<BucketizeOutput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <BucketizeOutput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into BucketizeOutput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl BucketizeOutput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
#[serde(rename = "Category")]
pub struct Category {
    #[serde(rename = "id")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub id: Option<i64>,

    #[serde(rename = "name")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub name: Option<String>,

}

impl Category {
    #[allow(clippy::new_without_default)]
    pub fn new() -> Category {
        Category {
            id: None,
            name: None,
        }
    }
}

/// Converts the Category value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for Category {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![

            self.id.as_ref().map(|id| {
                vec![
                    "id".to_string(),
                    id.to_string(),
                ].join(",")
            }),


            self.name.as_ref().map(|name| {
                vec![
                    "name".to_string(),
                    name.to_string(),
                ].join(",")
            }),

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a Category value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for Category {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub id: Vec<i64>,
            pub name: Vec<String>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing Category".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    #[allow(clippy::redundant_clone)]
                    "id" => intermediate_rep.id.push(<i64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    #[allow(clippy::redundant_clone)]
                    "name" => intermediate_rep.name.push(<String as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    _ => return std::result::Result::Err("Unexpected key while parsing Category".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(Category {
            id: intermediate_rep.id.into_iter().next(),
            name: intermediate_rep.name.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<Category> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<Category>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<Category>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for Category - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<Category> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <Category as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into Category - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl Category {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct CorrelationInput {
    #[serde(rename = "data")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub data: Option<Vec<Vec<f64>>>,

}

impl CorrelationInput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> CorrelationInput {
        CorrelationInput {
            data: None,
        }
    }
}

/// Converts the CorrelationInput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for CorrelationInput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![
            // Skipping data in query parameter serialization

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a CorrelationInput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for CorrelationInput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub data: Vec<Vec<Vec<f64>>>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing CorrelationInput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    "data" => return std::result::Result::Err("Parsing a container in this style is not supported in CorrelationInput".to_string()),
                    _ => return std::result::Result::Err("Unexpected key while parsing CorrelationInput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(CorrelationInput {
            data: intermediate_rep.data.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<CorrelationInput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<CorrelationInput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<CorrelationInput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for CorrelationInput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<CorrelationInput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <CorrelationInput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into CorrelationInput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl CorrelationInput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct CorrelationMatrixInput {
    #[serde(rename = "x")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub x: Option<Vec<f64>>,

    #[serde(rename = "y")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub y: Option<Vec<f64>>,

}

impl CorrelationMatrixInput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> CorrelationMatrixInput {
        CorrelationMatrixInput {
            x: None,
            y: None,
        }
    }
}

/// Converts the CorrelationMatrixInput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for CorrelationMatrixInput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![

            self.x.as_ref().map(|x| {
                vec![
                    "x".to_string(),
                    x.iter().map(|x| x.to_string()).collect::<Vec<_>>().join(","),
                ].join(",")
            }),


            self.y.as_ref().map(|y| {
                vec![
                    "y".to_string(),
                    y.iter().map(|x| x.to_string()).collect::<Vec<_>>().join(","),
                ].join(",")
            }),

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a CorrelationMatrixInput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for CorrelationMatrixInput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub x: Vec<Vec<f64>>,
            pub y: Vec<Vec<f64>>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing CorrelationMatrixInput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    "x" => return std::result::Result::Err("Parsing a container in this style is not supported in CorrelationMatrixInput".to_string()),
                    "y" => return std::result::Result::Err("Parsing a container in this style is not supported in CorrelationMatrixInput".to_string()),
                    _ => return std::result::Result::Err("Unexpected key while parsing CorrelationMatrixInput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(CorrelationMatrixInput {
            x: intermediate_rep.x.into_iter().next(),
            y: intermediate_rep.y.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<CorrelationMatrixInput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<CorrelationMatrixInput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<CorrelationMatrixInput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for CorrelationMatrixInput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<CorrelationMatrixInput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <CorrelationMatrixInput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into CorrelationMatrixInput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl CorrelationMatrixInput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct CorrelationMatrixOutput {
    #[serde(rename = "x")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub x: Option<f64>,

    #[serde(rename = "result")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub result: Option<f64>,

}

impl CorrelationMatrixOutput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> CorrelationMatrixOutput {
        CorrelationMatrixOutput {
            x: None,
            result: None,
        }
    }
}

/// Converts the CorrelationMatrixOutput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for CorrelationMatrixOutput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![

            self.x.as_ref().map(|x| {
                vec![
                    "x".to_string(),
                    x.to_string(),
                ].join(",")
            }),


            self.result.as_ref().map(|result| {
                vec![
                    "result".to_string(),
                    result.to_string(),
                ].join(",")
            }),

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a CorrelationMatrixOutput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for CorrelationMatrixOutput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub x: Vec<f64>,
            pub result: Vec<f64>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing CorrelationMatrixOutput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    #[allow(clippy::redundant_clone)]
                    "x" => intermediate_rep.x.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    #[allow(clippy::redundant_clone)]
                    "result" => intermediate_rep.result.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    _ => return std::result::Result::Err("Unexpected key while parsing CorrelationMatrixOutput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(CorrelationMatrixOutput {
            x: intermediate_rep.x.into_iter().next(),
            result: intermediate_rep.result.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<CorrelationMatrixOutput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<CorrelationMatrixOutput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<CorrelationMatrixOutput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for CorrelationMatrixOutput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<CorrelationMatrixOutput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <CorrelationMatrixOutput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into CorrelationMatrixOutput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl CorrelationMatrixOutput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct CorrelationOutput {
    #[serde(rename = "x")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub x: Option<f64>,

    #[serde(rename = "result")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub result: Option<f64>,

}

impl CorrelationOutput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> CorrelationOutput {
        CorrelationOutput {
            x: None,
            result: None,
        }
    }
}

/// Converts the CorrelationOutput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for CorrelationOutput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![

            self.x.as_ref().map(|x| {
                vec![
                    "x".to_string(),
                    x.to_string(),
                ].join(",")
            }),


            self.result.as_ref().map(|result| {
                vec![
                    "result".to_string(),
                    result.to_string(),
                ].join(",")
            }),

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a CorrelationOutput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for CorrelationOutput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub x: Vec<f64>,
            pub result: Vec<f64>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing CorrelationOutput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    #[allow(clippy::redundant_clone)]
                    "x" => intermediate_rep.x.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    #[allow(clippy::redundant_clone)]
                    "result" => intermediate_rep.result.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    _ => return std::result::Result::Err("Unexpected key while parsing CorrelationOutput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(CorrelationOutput {
            x: intermediate_rep.x.into_iter().next(),
            result: intermediate_rep.result.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<CorrelationOutput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<CorrelationOutput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<CorrelationOutput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for CorrelationOutput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<CorrelationOutput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <CorrelationOutput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into CorrelationOutput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl CorrelationOutput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct CovarianceInput {
    #[serde(rename = "x")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub x: Option<Vec<f64>>,

    #[serde(rename = "y")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub y: Option<Vec<f64>>,

}

impl CovarianceInput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> CovarianceInput {
        CovarianceInput {
            x: None,
            y: None,
        }
    }
}

/// Converts the CovarianceInput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for CovarianceInput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![

            self.x.as_ref().map(|x| {
                vec![
                    "x".to_string(),
                    x.iter().map(|x| x.to_string()).collect::<Vec<_>>().join(","),
                ].join(",")
            }),


            self.y.as_ref().map(|y| {
                vec![
                    "y".to_string(),
                    y.iter().map(|x| x.to_string()).collect::<Vec<_>>().join(","),
                ].join(",")
            }),

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a CovarianceInput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for CovarianceInput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub x: Vec<Vec<f64>>,
            pub y: Vec<Vec<f64>>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing CovarianceInput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    "x" => return std::result::Result::Err("Parsing a container in this style is not supported in CovarianceInput".to_string()),
                    "y" => return std::result::Result::Err("Parsing a container in this style is not supported in CovarianceInput".to_string()),
                    _ => return std::result::Result::Err("Unexpected key while parsing CovarianceInput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(CovarianceInput {
            x: intermediate_rep.x.into_iter().next(),
            y: intermediate_rep.y.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<CovarianceInput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<CovarianceInput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<CovarianceInput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for CovarianceInput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<CovarianceInput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <CovarianceInput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into CovarianceInput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl CovarianceInput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct CovarianceOutput {
    #[serde(rename = "x")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub x: Option<f64>,

    #[serde(rename = "result")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub result: Option<f64>,

}

impl CovarianceOutput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> CovarianceOutput {
        CovarianceOutput {
            x: None,
            result: None,
        }
    }
}

/// Converts the CovarianceOutput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for CovarianceOutput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![

            self.x.as_ref().map(|x| {
                vec![
                    "x".to_string(),
                    x.to_string(),
                ].join(",")
            }),


            self.result.as_ref().map(|result| {
                vec![
                    "result".to_string(),
                    result.to_string(),
                ].join(",")
            }),

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a CovarianceOutput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for CovarianceOutput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub x: Vec<f64>,
            pub result: Vec<f64>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing CovarianceOutput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    #[allow(clippy::redundant_clone)]
                    "x" => intermediate_rep.x.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    #[allow(clippy::redundant_clone)]
                    "result" => intermediate_rep.result.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    _ => return std::result::Result::Err("Unexpected key while parsing CovarianceOutput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(CovarianceOutput {
            x: intermediate_rep.x.into_iter().next(),
            result: intermediate_rep.result.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<CovarianceOutput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<CovarianceOutput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<CovarianceOutput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for CovarianceOutput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<CovarianceOutput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <CovarianceOutput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into CovarianceOutput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl CovarianceOutput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct DataRangeInput {
    #[serde(rename = "x")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub x: Option<Vec<f64>>,

}

impl DataRangeInput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> DataRangeInput {
        DataRangeInput {
            x: None,
        }
    }
}

/// Converts the DataRangeInput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for DataRangeInput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![

            self.x.as_ref().map(|x| {
                vec![
                    "x".to_string(),
                    x.iter().map(|x| x.to_string()).collect::<Vec<_>>().join(","),
                ].join(",")
            }),

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a DataRangeInput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for DataRangeInput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub x: Vec<Vec<f64>>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing DataRangeInput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    "x" => return std::result::Result::Err("Parsing a container in this style is not supported in DataRangeInput".to_string()),
                    _ => return std::result::Result::Err("Unexpected key while parsing DataRangeInput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(DataRangeInput {
            x: intermediate_rep.x.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<DataRangeInput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<DataRangeInput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<DataRangeInput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for DataRangeInput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<DataRangeInput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <DataRangeInput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into DataRangeInput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl DataRangeInput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct DataRangeOutput {
    #[serde(rename = "x")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub x: Option<f64>,

    #[serde(rename = "result")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub result: Option<f64>,

}

impl DataRangeOutput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> DataRangeOutput {
        DataRangeOutput {
            x: None,
            result: None,
        }
    }
}

/// Converts the DataRangeOutput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for DataRangeOutput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![

            self.x.as_ref().map(|x| {
                vec![
                    "x".to_string(),
                    x.to_string(),
                ].join(",")
            }),


            self.result.as_ref().map(|result| {
                vec![
                    "result".to_string(),
                    result.to_string(),
                ].join(",")
            }),

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a DataRangeOutput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for DataRangeOutput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub x: Vec<f64>,
            pub result: Vec<f64>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing DataRangeOutput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    #[allow(clippy::redundant_clone)]
                    "x" => intermediate_rep.x.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    #[allow(clippy::redundant_clone)]
                    "result" => intermediate_rep.result.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    _ => return std::result::Result::Err("Unexpected key while parsing DataRangeOutput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(DataRangeOutput {
            x: intermediate_rep.x.into_iter().next(),
            result: intermediate_rep.result.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<DataRangeOutput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<DataRangeOutput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<DataRangeOutput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for DataRangeOutput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<DataRangeOutput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <DataRangeOutput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into DataRangeOutput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl DataRangeOutput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct DeMeanInput {
    #[serde(rename = "x")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub x: Option<f64>,

}

impl DeMeanInput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> DeMeanInput {
        DeMeanInput {
            x: None,
        }
    }
}

/// Converts the DeMeanInput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for DeMeanInput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![

            self.x.as_ref().map(|x| {
                vec![
                    "x".to_string(),
                    x.to_string(),
                ].join(",")
            }),

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a DeMeanInput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for DeMeanInput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub x: Vec<f64>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing DeMeanInput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    #[allow(clippy::redundant_clone)]
                    "x" => intermediate_rep.x.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    _ => return std::result::Result::Err("Unexpected key while parsing DeMeanInput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(DeMeanInput {
            x: intermediate_rep.x.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<DeMeanInput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<DeMeanInput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<DeMeanInput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for DeMeanInput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<DeMeanInput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <DeMeanInput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into DeMeanInput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl DeMeanInput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct DeMeanOutput {
    #[serde(rename = "x")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub x: Option<f64>,

    #[serde(rename = "result")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub result: Option<f64>,

}

impl DeMeanOutput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> DeMeanOutput {
        DeMeanOutput {
            x: None,
            result: None,
        }
    }
}

/// Converts the DeMeanOutput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for DeMeanOutput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![

            self.x.as_ref().map(|x| {
                vec![
                    "x".to_string(),
                    x.to_string(),
                ].join(",")
            }),


            self.result.as_ref().map(|result| {
                vec![
                    "result".to_string(),
                    result.to_string(),
                ].join(",")
            }),

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a DeMeanOutput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for DeMeanOutput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub x: Vec<f64>,
            pub result: Vec<f64>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing DeMeanOutput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    #[allow(clippy::redundant_clone)]
                    "x" => intermediate_rep.x.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    #[allow(clippy::redundant_clone)]
                    "result" => intermediate_rep.result.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    _ => return std::result::Result::Err("Unexpected key while parsing DeMeanOutput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(DeMeanOutput {
            x: intermediate_rep.x.into_iter().next(),
            result: intermediate_rep.result.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<DeMeanOutput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<DeMeanOutput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<DeMeanOutput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for DeMeanOutput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<DeMeanOutput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <DeMeanOutput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into DeMeanOutput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl DeMeanOutput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct DifferenceQuotientInput {
    #[serde(rename = "x")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub x: Option<f64>,

    #[serde(rename = "h")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub h: Option<f64>,

}

impl DifferenceQuotientInput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> DifferenceQuotientInput {
        DifferenceQuotientInput {
            x: None,
            h: None,
        }
    }
}

/// Converts the DifferenceQuotientInput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for DifferenceQuotientInput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![

            self.x.as_ref().map(|x| {
                vec![
                    "x".to_string(),
                    x.to_string(),
                ].join(",")
            }),


            self.h.as_ref().map(|h| {
                vec![
                    "h".to_string(),
                    h.to_string(),
                ].join(",")
            }),

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a DifferenceQuotientInput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for DifferenceQuotientInput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub x: Vec<f64>,
            pub h: Vec<f64>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing DifferenceQuotientInput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    #[allow(clippy::redundant_clone)]
                    "x" => intermediate_rep.x.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    #[allow(clippy::redundant_clone)]
                    "h" => intermediate_rep.h.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    _ => return std::result::Result::Err("Unexpected key while parsing DifferenceQuotientInput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(DifferenceQuotientInput {
            x: intermediate_rep.x.into_iter().next(),
            h: intermediate_rep.h.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<DifferenceQuotientInput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<DifferenceQuotientInput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<DifferenceQuotientInput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for DifferenceQuotientInput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<DifferenceQuotientInput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <DifferenceQuotientInput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into DifferenceQuotientInput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl DifferenceQuotientInput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct DifferenceQuotientOutput {
    #[serde(rename = "x")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub x: Option<f64>,

    #[serde(rename = "result")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub result: Option<f64>,

}

impl DifferenceQuotientOutput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> DifferenceQuotientOutput {
        DifferenceQuotientOutput {
            x: None,
            result: None,
        }
    }
}

/// Converts the DifferenceQuotientOutput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for DifferenceQuotientOutput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![

            self.x.as_ref().map(|x| {
                vec![
                    "x".to_string(),
                    x.to_string(),
                ].join(",")
            }),


            self.result.as_ref().map(|result| {
                vec![
                    "result".to_string(),
                    result.to_string(),
                ].join(",")
            }),

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a DifferenceQuotientOutput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for DifferenceQuotientOutput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub x: Vec<f64>,
            pub result: Vec<f64>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing DifferenceQuotientOutput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    #[allow(clippy::redundant_clone)]
                    "x" => intermediate_rep.x.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    #[allow(clippy::redundant_clone)]
                    "result" => intermediate_rep.result.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    _ => return std::result::Result::Err("Unexpected key while parsing DifferenceQuotientOutput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(DifferenceQuotientOutput {
            x: intermediate_rep.x.into_iter().next(),
            result: intermediate_rep.result.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<DifferenceQuotientOutput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<DifferenceQuotientOutput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<DifferenceQuotientOutput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for DifferenceQuotientOutput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<DifferenceQuotientOutput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <DifferenceQuotientOutput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into DifferenceQuotientOutput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl DifferenceQuotientOutput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct DistanceInput {
    #[serde(rename = "v")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub v: Option<Vec<f64>>,

    #[serde(rename = "w")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub w: Option<Vec<f64>>,

}

impl DistanceInput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> DistanceInput {
        DistanceInput {
            v: None,
            w: None,
        }
    }
}

/// Converts the DistanceInput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for DistanceInput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![

            self.v.as_ref().map(|v| {
                vec![
                    "v".to_string(),
                    v.iter().map(|x| x.to_string()).collect::<Vec<_>>().join(","),
                ].join(",")
            }),


            self.w.as_ref().map(|w| {
                vec![
                    "w".to_string(),
                    w.iter().map(|x| x.to_string()).collect::<Vec<_>>().join(","),
                ].join(",")
            }),

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a DistanceInput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for DistanceInput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub v: Vec<Vec<f64>>,
            pub w: Vec<Vec<f64>>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing DistanceInput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    "v" => return std::result::Result::Err("Parsing a container in this style is not supported in DistanceInput".to_string()),
                    "w" => return std::result::Result::Err("Parsing a container in this style is not supported in DistanceInput".to_string()),
                    _ => return std::result::Result::Err("Unexpected key while parsing DistanceInput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(DistanceInput {
            v: intermediate_rep.v.into_iter().next(),
            w: intermediate_rep.w.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<DistanceInput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<DistanceInput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<DistanceInput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for DistanceInput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<DistanceInput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <DistanceInput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into DistanceInput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl DistanceInput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct DistanceOutput {
    #[serde(rename = "x")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub x: Option<f64>,

    #[serde(rename = "result")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub result: Option<f64>,

}

impl DistanceOutput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> DistanceOutput {
        DistanceOutput {
            x: None,
            result: None,
        }
    }
}

/// Converts the DistanceOutput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for DistanceOutput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![

            self.x.as_ref().map(|x| {
                vec![
                    "x".to_string(),
                    x.to_string(),
                ].join(",")
            }),


            self.result.as_ref().map(|result| {
                vec![
                    "result".to_string(),
                    result.to_string(),
                ].join(",")
            }),

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a DistanceOutput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for DistanceOutput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub x: Vec<f64>,
            pub result: Vec<f64>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing DistanceOutput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    #[allow(clippy::redundant_clone)]
                    "x" => intermediate_rep.x.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    #[allow(clippy::redundant_clone)]
                    "result" => intermediate_rep.result.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    _ => return std::result::Result::Err("Unexpected key while parsing DistanceOutput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(DistanceOutput {
            x: intermediate_rep.x.into_iter().next(),
            result: intermediate_rep.result.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<DistanceOutput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<DistanceOutput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<DistanceOutput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for DistanceOutput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<DistanceOutput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <DistanceOutput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into DistanceOutput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl DistanceOutput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct DotInput {
    #[serde(rename = "v")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub v: Option<Vec<f64>>,

    #[serde(rename = "w")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub w: Option<Vec<f64>>,

}

impl DotInput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> DotInput {
        DotInput {
            v: None,
            w: None,
        }
    }
}

/// Converts the DotInput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for DotInput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![

            self.v.as_ref().map(|v| {
                vec![
                    "v".to_string(),
                    v.iter().map(|x| x.to_string()).collect::<Vec<_>>().join(","),
                ].join(",")
            }),


            self.w.as_ref().map(|w| {
                vec![
                    "w".to_string(),
                    w.iter().map(|x| x.to_string()).collect::<Vec<_>>().join(","),
                ].join(",")
            }),

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a DotInput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for DotInput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub v: Vec<Vec<f64>>,
            pub w: Vec<Vec<f64>>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing DotInput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    "v" => return std::result::Result::Err("Parsing a container in this style is not supported in DotInput".to_string()),
                    "w" => return std::result::Result::Err("Parsing a container in this style is not supported in DotInput".to_string()),
                    _ => return std::result::Result::Err("Unexpected key while parsing DotInput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(DotInput {
            v: intermediate_rep.v.into_iter().next(),
            w: intermediate_rep.w.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<DotInput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<DotInput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<DotInput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for DotInput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<DotInput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <DotInput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into DotInput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl DotInput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct DotOutput {
    #[serde(rename = "x")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub x: Option<f64>,

    #[serde(rename = "result")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub result: Option<f64>,

}

impl DotOutput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> DotOutput {
        DotOutput {
            x: None,
            result: None,
        }
    }
}

/// Converts the DotOutput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for DotOutput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![

            self.x.as_ref().map(|x| {
                vec![
                    "x".to_string(),
                    x.to_string(),
                ].join(",")
            }),


            self.result.as_ref().map(|result| {
                vec![
                    "result".to_string(),
                    result.to_string(),
                ].join(",")
            }),

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a DotOutput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for DotOutput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub x: Vec<f64>,
            pub result: Vec<f64>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing DotOutput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    #[allow(clippy::redundant_clone)]
                    "x" => intermediate_rep.x.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    #[allow(clippy::redundant_clone)]
                    "result" => intermediate_rep.result.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    _ => return std::result::Result::Err("Unexpected key while parsing DotOutput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(DotOutput {
            x: intermediate_rep.x.into_iter().next(),
            result: intermediate_rep.result.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<DotOutput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<DotOutput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<DotOutput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for DotOutput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<DotOutput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <DotOutput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into DotOutput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl DotOutput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct EstimateGradientInput {
    #[serde(rename = "v")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub v: Option<Vec<f64>>,

    #[serde(rename = "h")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub h: Option<f64>,

}

impl EstimateGradientInput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> EstimateGradientInput {
        EstimateGradientInput {
            v: None,
            h: None,
        }
    }
}

/// Converts the EstimateGradientInput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for EstimateGradientInput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![

            self.v.as_ref().map(|v| {
                vec![
                    "v".to_string(),
                    v.iter().map(|x| x.to_string()).collect::<Vec<_>>().join(","),
                ].join(",")
            }),


            self.h.as_ref().map(|h| {
                vec![
                    "h".to_string(),
                    h.to_string(),
                ].join(",")
            }),

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a EstimateGradientInput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for EstimateGradientInput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub v: Vec<Vec<f64>>,
            pub h: Vec<f64>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing EstimateGradientInput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    "v" => return std::result::Result::Err("Parsing a container in this style is not supported in EstimateGradientInput".to_string()),
                    #[allow(clippy::redundant_clone)]
                    "h" => intermediate_rep.h.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    _ => return std::result::Result::Err("Unexpected key while parsing EstimateGradientInput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(EstimateGradientInput {
            v: intermediate_rep.v.into_iter().next(),
            h: intermediate_rep.h.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<EstimateGradientInput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<EstimateGradientInput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<EstimateGradientInput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for EstimateGradientInput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<EstimateGradientInput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <EstimateGradientInput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into EstimateGradientInput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl EstimateGradientInput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct EstimateGradientOutput {
    #[serde(rename = "x")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub x: Option<f64>,

    #[serde(rename = "result")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub result: Option<f64>,

}

impl EstimateGradientOutput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> EstimateGradientOutput {
        EstimateGradientOutput {
            x: None,
            result: None,
        }
    }
}

/// Converts the EstimateGradientOutput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for EstimateGradientOutput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![

            self.x.as_ref().map(|x| {
                vec![
                    "x".to_string(),
                    x.to_string(),
                ].join(",")
            }),


            self.result.as_ref().map(|result| {
                vec![
                    "result".to_string(),
                    result.to_string(),
                ].join(",")
            }),

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a EstimateGradientOutput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for EstimateGradientOutput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub x: Vec<f64>,
            pub result: Vec<f64>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing EstimateGradientOutput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    #[allow(clippy::redundant_clone)]
                    "x" => intermediate_rep.x.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    #[allow(clippy::redundant_clone)]
                    "result" => intermediate_rep.result.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    _ => return std::result::Result::Err("Unexpected key while parsing EstimateGradientOutput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(EstimateGradientOutput {
            x: intermediate_rep.x.into_iter().next(),
            result: intermediate_rep.result.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<EstimateGradientOutput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<EstimateGradientOutput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<EstimateGradientOutput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for EstimateGradientOutput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<EstimateGradientOutput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <EstimateGradientOutput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into EstimateGradientOutput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl EstimateGradientOutput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct F1ScoreInput {
    /// number of True Positives
    #[serde(rename = "tp")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub tp: Option<f64>,

    /// number of False Positives
    #[serde(rename = "fp")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub fp: Option<f64>,

    /// number of False Negatives
    #[serde(rename = "fn")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub r#fn: Option<f64>,

    /// number of True Negatives
    #[serde(rename = "tn")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub tn: Option<f64>,

}

impl F1ScoreInput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> F1ScoreInput {
        F1ScoreInput {
            tp: None,
            fp: None,
            r#fn: None,
            tn: None,
        }
    }
}

/// Converts the F1ScoreInput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for F1ScoreInput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![

            self.tp.as_ref().map(|tp| {
                vec![
                    "tp".to_string(),
                    tp.to_string(),
                ].join(",")
            }),


            self.fp.as_ref().map(|fp| {
                vec![
                    "fp".to_string(),
                    fp.to_string(),
                ].join(",")
            }),


            self.r#fn.as_ref().map(|r#fn| {
                vec![
                    "fn".to_string(),
                    r#fn.to_string(),
                ].join(",")
            }),


            self.tn.as_ref().map(|tn| {
                vec![
                    "tn".to_string(),
                    tn.to_string(),
                ].join(",")
            }),

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a F1ScoreInput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for F1ScoreInput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub tp: Vec<f64>,
            pub fp: Vec<f64>,
            pub r#fn: Vec<f64>,
            pub tn: Vec<f64>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing F1ScoreInput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    #[allow(clippy::redundant_clone)]
                    "tp" => intermediate_rep.tp.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    #[allow(clippy::redundant_clone)]
                    "fp" => intermediate_rep.fp.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    #[allow(clippy::redundant_clone)]
                    "fn" => intermediate_rep.r#fn.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    #[allow(clippy::redundant_clone)]
                    "tn" => intermediate_rep.tn.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    _ => return std::result::Result::Err("Unexpected key while parsing F1ScoreInput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(F1ScoreInput {
            tp: intermediate_rep.tp.into_iter().next(),
            fp: intermediate_rep.fp.into_iter().next(),
            r#fn: intermediate_rep.r#fn.into_iter().next(),
            tn: intermediate_rep.tn.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<F1ScoreInput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<F1ScoreInput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<F1ScoreInput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for F1ScoreInput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<F1ScoreInput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <F1ScoreInput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into F1ScoreInput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl F1ScoreInput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, PartialOrd, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct F1ScoreOutput(f64);

impl std::convert::From<f64> for F1ScoreOutput {
    fn from(x: f64) -> Self {
        F1ScoreOutput(x)
    }
}

impl std::convert::From<F1ScoreOutput> for f64 {
    fn from(x: F1ScoreOutput) -> Self {
        x.0
    }
}

impl std::ops::Deref for F1ScoreOutput {
    type Target = f64;
    fn deref(&self) -> &f64 {
        &self.0
    }
}

impl std::ops::DerefMut for F1ScoreOutput {
    fn deref_mut(&mut self) -> &mut f64 {
        &mut self.0
    }
}


impl F1ScoreOutput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct GetColumnInput {
    #[serde(rename = "mat")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub mat: Option<Vec<Vec<f64>>>,

    #[serde(rename = "col")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub col: Option<f64>,

}

impl GetColumnInput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> GetColumnInput {
        GetColumnInput {
            mat: None,
            col: None,
        }
    }
}

/// Converts the GetColumnInput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for GetColumnInput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![
            // Skipping mat in query parameter serialization


            self.col.as_ref().map(|col| {
                vec![
                    "col".to_string(),
                    col.to_string(),
                ].join(",")
            }),

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a GetColumnInput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for GetColumnInput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub mat: Vec<Vec<Vec<f64>>>,
            pub col: Vec<f64>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing GetColumnInput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    "mat" => return std::result::Result::Err("Parsing a container in this style is not supported in GetColumnInput".to_string()),
                    #[allow(clippy::redundant_clone)]
                    "col" => intermediate_rep.col.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    _ => return std::result::Result::Err("Unexpected key while parsing GetColumnInput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(GetColumnInput {
            mat: intermediate_rep.mat.into_iter().next(),
            col: intermediate_rep.col.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<GetColumnInput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<GetColumnInput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<GetColumnInput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for GetColumnInput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<GetColumnInput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <GetColumnInput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into GetColumnInput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl GetColumnInput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct GetColumnOutput {
    #[serde(rename = "x")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub x: Option<f64>,

    #[serde(rename = "result")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub result: Option<f64>,

}

impl GetColumnOutput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> GetColumnOutput {
        GetColumnOutput {
            x: None,
            result: None,
        }
    }
}

/// Converts the GetColumnOutput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for GetColumnOutput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![

            self.x.as_ref().map(|x| {
                vec![
                    "x".to_string(),
                    x.to_string(),
                ].join(",")
            }),


            self.result.as_ref().map(|result| {
                vec![
                    "result".to_string(),
                    result.to_string(),
                ].join(",")
            }),

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a GetColumnOutput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for GetColumnOutput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub x: Vec<f64>,
            pub result: Vec<f64>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing GetColumnOutput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    #[allow(clippy::redundant_clone)]
                    "x" => intermediate_rep.x.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    #[allow(clippy::redundant_clone)]
                    "result" => intermediate_rep.result.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    _ => return std::result::Result::Err("Unexpected key while parsing GetColumnOutput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(GetColumnOutput {
            x: intermediate_rep.x.into_iter().next(),
            result: intermediate_rep.result.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<GetColumnOutput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<GetColumnOutput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<GetColumnOutput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for GetColumnOutput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<GetColumnOutput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <GetColumnOutput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into GetColumnOutput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl GetColumnOutput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct GetRowInput {
    #[serde(rename = "mat")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub mat: Option<Vec<Vec<f64>>>,

    #[serde(rename = "row")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub row: Option<f64>,

}

impl GetRowInput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> GetRowInput {
        GetRowInput {
            mat: None,
            row: None,
        }
    }
}

/// Converts the GetRowInput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for GetRowInput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![
            // Skipping mat in query parameter serialization


            self.row.as_ref().map(|row| {
                vec![
                    "row".to_string(),
                    row.to_string(),
                ].join(",")
            }),

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a GetRowInput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for GetRowInput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub mat: Vec<Vec<Vec<f64>>>,
            pub row: Vec<f64>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing GetRowInput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    "mat" => return std::result::Result::Err("Parsing a container in this style is not supported in GetRowInput".to_string()),
                    #[allow(clippy::redundant_clone)]
                    "row" => intermediate_rep.row.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    _ => return std::result::Result::Err("Unexpected key while parsing GetRowInput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(GetRowInput {
            mat: intermediate_rep.mat.into_iter().next(),
            row: intermediate_rep.row.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<GetRowInput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<GetRowInput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<GetRowInput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for GetRowInput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<GetRowInput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <GetRowInput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into GetRowInput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl GetRowInput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct GetRowOutput {
    #[serde(rename = "x")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub x: Option<f64>,

    #[serde(rename = "result")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub result: Option<f64>,

}

impl GetRowOutput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> GetRowOutput {
        GetRowOutput {
            x: None,
            result: None,
        }
    }
}

/// Converts the GetRowOutput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for GetRowOutput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![

            self.x.as_ref().map(|x| {
                vec![
                    "x".to_string(),
                    x.to_string(),
                ].join(",")
            }),


            self.result.as_ref().map(|result| {
                vec![
                    "result".to_string(),
                    result.to_string(),
                ].join(",")
            }),

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a GetRowOutput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for GetRowOutput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub x: Vec<f64>,
            pub result: Vec<f64>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing GetRowOutput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    #[allow(clippy::redundant_clone)]
                    "x" => intermediate_rep.x.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    #[allow(clippy::redundant_clone)]
                    "result" => intermediate_rep.result.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    _ => return std::result::Result::Err("Unexpected key while parsing GetRowOutput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(GetRowOutput {
            x: intermediate_rep.x.into_iter().next(),
            result: intermediate_rep.result.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<GetRowOutput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<GetRowOutput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<GetRowOutput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for GetRowOutput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<GetRowOutput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <GetRowOutput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into GetRowOutput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl GetRowOutput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct InRandomOrderInput {
    #[serde(rename = "data")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub data: Option<Vec<f64>>,

}

impl InRandomOrderInput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> InRandomOrderInput {
        InRandomOrderInput {
            data: None,
        }
    }
}

/// Converts the InRandomOrderInput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for InRandomOrderInput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![

            self.data.as_ref().map(|data| {
                vec![
                    "data".to_string(),
                    data.iter().map(|x| x.to_string()).collect::<Vec<_>>().join(","),
                ].join(",")
            }),

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a InRandomOrderInput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for InRandomOrderInput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub data: Vec<Vec<f64>>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing InRandomOrderInput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    "data" => return std::result::Result::Err("Parsing a container in this style is not supported in InRandomOrderInput".to_string()),
                    _ => return std::result::Result::Err("Unexpected key while parsing InRandomOrderInput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(InRandomOrderInput {
            data: intermediate_rep.data.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<InRandomOrderInput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<InRandomOrderInput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<InRandomOrderInput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for InRandomOrderInput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<InRandomOrderInput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <InRandomOrderInput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into InRandomOrderInput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl InRandomOrderInput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct InterquartileRangeInput {
    #[serde(rename = "x")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub x: Option<Vec<f64>>,

}

impl InterquartileRangeInput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> InterquartileRangeInput {
        InterquartileRangeInput {
            x: None,
        }
    }
}

/// Converts the InterquartileRangeInput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for InterquartileRangeInput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![

            self.x.as_ref().map(|x| {
                vec![
                    "x".to_string(),
                    x.iter().map(|x| x.to_string()).collect::<Vec<_>>().join(","),
                ].join(",")
            }),

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a InterquartileRangeInput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for InterquartileRangeInput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub x: Vec<Vec<f64>>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing InterquartileRangeInput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    "x" => return std::result::Result::Err("Parsing a container in this style is not supported in InterquartileRangeInput".to_string()),
                    _ => return std::result::Result::Err("Unexpected key while parsing InterquartileRangeInput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(InterquartileRangeInput {
            x: intermediate_rep.x.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<InterquartileRangeInput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<InterquartileRangeInput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<InterquartileRangeInput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for InterquartileRangeInput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<InterquartileRangeInput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <InterquartileRangeInput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into InterquartileRangeInput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl InterquartileRangeInput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, PartialOrd, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct InterquartileRangeOutput(f64);

impl std::convert::From<f64> for InterquartileRangeOutput {
    fn from(x: f64) -> Self {
        InterquartileRangeOutput(x)
    }
}

impl std::convert::From<InterquartileRangeOutput> for f64 {
    fn from(x: InterquartileRangeOutput) -> Self {
        x.0
    }
}

impl std::ops::Deref for InterquartileRangeOutput {
    type Target = f64;
    fn deref(&self) -> &f64 {
        &self.0
    }
}

impl std::ops::DerefMut for InterquartileRangeOutput {
    fn deref_mut(&mut self) -> &mut f64 {
        &mut self.0
    }
}


impl InterquartileRangeOutput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct MagnitudeInput {
    #[serde(rename = "v")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub v: Option<Vec<f64>>,

}

impl MagnitudeInput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> MagnitudeInput {
        MagnitudeInput {
            v: None,
        }
    }
}

/// Converts the MagnitudeInput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for MagnitudeInput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![

            self.v.as_ref().map(|v| {
                vec![
                    "v".to_string(),
                    v.iter().map(|x| x.to_string()).collect::<Vec<_>>().join(","),
                ].join(",")
            }),

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a MagnitudeInput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for MagnitudeInput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub v: Vec<Vec<f64>>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing MagnitudeInput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    "v" => return std::result::Result::Err("Parsing a container in this style is not supported in MagnitudeInput".to_string()),
                    _ => return std::result::Result::Err("Unexpected key while parsing MagnitudeInput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(MagnitudeInput {
            v: intermediate_rep.v.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<MagnitudeInput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<MagnitudeInput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<MagnitudeInput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for MagnitudeInput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<MagnitudeInput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <MagnitudeInput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into MagnitudeInput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl MagnitudeInput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, PartialOrd, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct MagnitudeOutput(f64);

impl std::convert::From<f64> for MagnitudeOutput {
    fn from(x: f64) -> Self {
        MagnitudeOutput(x)
    }
}

impl std::convert::From<MagnitudeOutput> for f64 {
    fn from(x: MagnitudeOutput) -> Self {
        x.0
    }
}

impl std::ops::Deref for MagnitudeOutput {
    type Target = f64;
    fn deref(&self) -> &f64 {
        &self.0
    }
}

impl std::ops::DerefMut for MagnitudeOutput {
    fn deref_mut(&mut self) -> &mut f64 {
        &mut self.0
    }
}


impl MagnitudeOutput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct MatrixAddInput {
    #[serde(rename = "mat1")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub mat1: Option<Vec<Vec<f64>>>,

    #[serde(rename = "mat2")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub mat2: Option<Vec<Vec<f64>>>,

}

impl MatrixAddInput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> MatrixAddInput {
        MatrixAddInput {
            mat1: None,
            mat2: None,
        }
    }
}

/// Converts the MatrixAddInput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for MatrixAddInput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![
            // Skipping mat1 in query parameter serialization

            // Skipping mat2 in query parameter serialization

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a MatrixAddInput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for MatrixAddInput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub mat1: Vec<Vec<Vec<f64>>>,
            pub mat2: Vec<Vec<Vec<f64>>>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing MatrixAddInput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    "mat1" => return std::result::Result::Err("Parsing a container in this style is not supported in MatrixAddInput".to_string()),
                    "mat2" => return std::result::Result::Err("Parsing a container in this style is not supported in MatrixAddInput".to_string()),
                    _ => return std::result::Result::Err("Unexpected key while parsing MatrixAddInput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(MatrixAddInput {
            mat1: intermediate_rep.mat1.into_iter().next(),
            mat2: intermediate_rep.mat2.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<MatrixAddInput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<MatrixAddInput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<MatrixAddInput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for MatrixAddInput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<MatrixAddInput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <MatrixAddInput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into MatrixAddInput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl MatrixAddInput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct MaximizeBatchInput {
    #[serde(rename = "x")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub x: Option<Vec<Vec<f64>>>,

}

impl MaximizeBatchInput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> MaximizeBatchInput {
        MaximizeBatchInput {
            x: None,
        }
    }
}

/// Converts the MaximizeBatchInput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for MaximizeBatchInput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![
            // Skipping x in query parameter serialization

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a MaximizeBatchInput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for MaximizeBatchInput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub x: Vec<Vec<Vec<f64>>>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing MaximizeBatchInput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    "x" => return std::result::Result::Err("Parsing a container in this style is not supported in MaximizeBatchInput".to_string()),
                    _ => return std::result::Result::Err("Unexpected key while parsing MaximizeBatchInput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(MaximizeBatchInput {
            x: intermediate_rep.x.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<MaximizeBatchInput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<MaximizeBatchInput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<MaximizeBatchInput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for MaximizeBatchInput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<MaximizeBatchInput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <MaximizeBatchInput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into MaximizeBatchInput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl MaximizeBatchInput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct MaximizeBatchOutput {
    #[serde(rename = "x")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub x: Option<f64>,

    #[serde(rename = "result")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub result: Option<f64>,

}

impl MaximizeBatchOutput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> MaximizeBatchOutput {
        MaximizeBatchOutput {
            x: None,
            result: None,
        }
    }
}

/// Converts the MaximizeBatchOutput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for MaximizeBatchOutput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![

            self.x.as_ref().map(|x| {
                vec![
                    "x".to_string(),
                    x.to_string(),
                ].join(",")
            }),


            self.result.as_ref().map(|result| {
                vec![
                    "result".to_string(),
                    result.to_string(),
                ].join(",")
            }),

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a MaximizeBatchOutput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for MaximizeBatchOutput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub x: Vec<f64>,
            pub result: Vec<f64>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing MaximizeBatchOutput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    #[allow(clippy::redundant_clone)]
                    "x" => intermediate_rep.x.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    #[allow(clippy::redundant_clone)]
                    "result" => intermediate_rep.result.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    _ => return std::result::Result::Err("Unexpected key while parsing MaximizeBatchOutput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(MaximizeBatchOutput {
            x: intermediate_rep.x.into_iter().next(),
            result: intermediate_rep.result.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<MaximizeBatchOutput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<MaximizeBatchOutput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<MaximizeBatchOutput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for MaximizeBatchOutput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<MaximizeBatchOutput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <MaximizeBatchOutput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into MaximizeBatchOutput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl MaximizeBatchOutput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct MaximizeStochasticInput {
    #[serde(rename = "x")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub x: Option<Vec<Vec<f64>>>,

    #[serde(rename = "y")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub y: Option<Vec<f64>>,

}

impl MaximizeStochasticInput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> MaximizeStochasticInput {
        MaximizeStochasticInput {
            x: None,
            y: None,
        }
    }
}

/// Converts the MaximizeStochasticInput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for MaximizeStochasticInput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![
            // Skipping x in query parameter serialization


            self.y.as_ref().map(|y| {
                vec![
                    "y".to_string(),
                    y.iter().map(|x| x.to_string()).collect::<Vec<_>>().join(","),
                ].join(",")
            }),

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a MaximizeStochasticInput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for MaximizeStochasticInput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub x: Vec<Vec<Vec<f64>>>,
            pub y: Vec<Vec<f64>>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing MaximizeStochasticInput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    "x" => return std::result::Result::Err("Parsing a container in this style is not supported in MaximizeStochasticInput".to_string()),
                    "y" => return std::result::Result::Err("Parsing a container in this style is not supported in MaximizeStochasticInput".to_string()),
                    _ => return std::result::Result::Err("Unexpected key while parsing MaximizeStochasticInput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(MaximizeStochasticInput {
            x: intermediate_rep.x.into_iter().next(),
            y: intermediate_rep.y.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<MaximizeStochasticInput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<MaximizeStochasticInput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<MaximizeStochasticInput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for MaximizeStochasticInput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<MaximizeStochasticInput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <MaximizeStochasticInput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into MaximizeStochasticInput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl MaximizeStochasticInput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct MaximizeStochasticOutput {
    #[serde(rename = "x")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub x: Option<f64>,

    #[serde(rename = "result")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub result: Option<f64>,

}

impl MaximizeStochasticOutput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> MaximizeStochasticOutput {
        MaximizeStochasticOutput {
            x: None,
            result: None,
        }
    }
}

/// Converts the MaximizeStochasticOutput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for MaximizeStochasticOutput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![

            self.x.as_ref().map(|x| {
                vec![
                    "x".to_string(),
                    x.to_string(),
                ].join(",")
            }),


            self.result.as_ref().map(|result| {
                vec![
                    "result".to_string(),
                    result.to_string(),
                ].join(",")
            }),

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a MaximizeStochasticOutput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for MaximizeStochasticOutput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub x: Vec<f64>,
            pub result: Vec<f64>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing MaximizeStochasticOutput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    #[allow(clippy::redundant_clone)]
                    "x" => intermediate_rep.x.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    #[allow(clippy::redundant_clone)]
                    "result" => intermediate_rep.result.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    _ => return std::result::Result::Err("Unexpected key while parsing MaximizeStochasticOutput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(MaximizeStochasticOutput {
            x: intermediate_rep.x.into_iter().next(),
            result: intermediate_rep.result.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<MaximizeStochasticOutput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<MaximizeStochasticOutput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<MaximizeStochasticOutput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for MaximizeStochasticOutput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<MaximizeStochasticOutput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <MaximizeStochasticOutput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into MaximizeStochasticOutput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl MaximizeStochasticOutput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct MeanInput {
    #[serde(rename = "x")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub x: Option<Vec<f64>>,

}

impl MeanInput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> MeanInput {
        MeanInput {
            x: None,
        }
    }
}

/// Converts the MeanInput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for MeanInput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![

            self.x.as_ref().map(|x| {
                vec![
                    "x".to_string(),
                    x.iter().map(|x| x.to_string()).collect::<Vec<_>>().join(","),
                ].join(",")
            }),

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a MeanInput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for MeanInput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub x: Vec<Vec<f64>>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing MeanInput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    "x" => return std::result::Result::Err("Parsing a container in this style is not supported in MeanInput".to_string()),
                    _ => return std::result::Result::Err("Unexpected key while parsing MeanInput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(MeanInput {
            x: intermediate_rep.x.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<MeanInput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<MeanInput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<MeanInput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for MeanInput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<MeanInput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <MeanInput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into MeanInput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl MeanInput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, PartialOrd, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct MeanOutput(f64);

impl std::convert::From<f64> for MeanOutput {
    fn from(x: f64) -> Self {
        MeanOutput(x)
    }
}

impl std::convert::From<MeanOutput> for f64 {
    fn from(x: MeanOutput) -> Self {
        x.0
    }
}

impl std::ops::Deref for MeanOutput {
    type Target = f64;
    fn deref(&self) -> &f64 {
        &self.0
    }
}

impl std::ops::DerefMut for MeanOutput {
    fn deref_mut(&mut self) -> &mut f64 {
        &mut self.0
    }
}


impl MeanOutput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct MedianInput {
    #[serde(rename = "x")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub x: Option<Vec<f64>>,

}

impl MedianInput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> MedianInput {
        MedianInput {
            x: None,
        }
    }
}

/// Converts the MedianInput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for MedianInput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![

            self.x.as_ref().map(|x| {
                vec![
                    "x".to_string(),
                    x.iter().map(|x| x.to_string()).collect::<Vec<_>>().join(","),
                ].join(",")
            }),

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a MedianInput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for MedianInput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub x: Vec<Vec<f64>>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing MedianInput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    "x" => return std::result::Result::Err("Parsing a container in this style is not supported in MedianInput".to_string()),
                    _ => return std::result::Result::Err("Unexpected key while parsing MedianInput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(MedianInput {
            x: intermediate_rep.x.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<MedianInput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<MedianInput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<MedianInput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for MedianInput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<MedianInput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <MedianInput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into MedianInput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl MedianInput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, PartialOrd, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct MedianOutput(f64);

impl std::convert::From<f64> for MedianOutput {
    fn from(x: f64) -> Self {
        MedianOutput(x)
    }
}

impl std::convert::From<MedianOutput> for f64 {
    fn from(x: MedianOutput) -> Self {
        x.0
    }
}

impl std::ops::Deref for MedianOutput {
    type Target = f64;
    fn deref(&self) -> &f64 {
        &self.0
    }
}

impl std::ops::DerefMut for MedianOutput {
    fn deref_mut(&mut self) -> &mut f64 {
        &mut self.0
    }
}


impl MedianOutput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct MinimizeBatchInput {
    #[serde(rename = "x")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub x: Option<f64>,

}

impl MinimizeBatchInput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> MinimizeBatchInput {
        MinimizeBatchInput {
            x: None,
        }
    }
}

/// Converts the MinimizeBatchInput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for MinimizeBatchInput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![

            self.x.as_ref().map(|x| {
                vec![
                    "x".to_string(),
                    x.to_string(),
                ].join(",")
            }),

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a MinimizeBatchInput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for MinimizeBatchInput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub x: Vec<f64>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing MinimizeBatchInput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    #[allow(clippy::redundant_clone)]
                    "x" => intermediate_rep.x.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    _ => return std::result::Result::Err("Unexpected key while parsing MinimizeBatchInput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(MinimizeBatchInput {
            x: intermediate_rep.x.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<MinimizeBatchInput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<MinimizeBatchInput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<MinimizeBatchInput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for MinimizeBatchInput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<MinimizeBatchInput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <MinimizeBatchInput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into MinimizeBatchInput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl MinimizeBatchInput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct MinimizeBatchOutput {
    #[serde(rename = "x")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub x: Option<f64>,

    #[serde(rename = "result")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub result: Option<f64>,

}

impl MinimizeBatchOutput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> MinimizeBatchOutput {
        MinimizeBatchOutput {
            x: None,
            result: None,
        }
    }
}

/// Converts the MinimizeBatchOutput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for MinimizeBatchOutput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![

            self.x.as_ref().map(|x| {
                vec![
                    "x".to_string(),
                    x.to_string(),
                ].join(",")
            }),


            self.result.as_ref().map(|result| {
                vec![
                    "result".to_string(),
                    result.to_string(),
                ].join(",")
            }),

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a MinimizeBatchOutput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for MinimizeBatchOutput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub x: Vec<f64>,
            pub result: Vec<f64>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing MinimizeBatchOutput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    #[allow(clippy::redundant_clone)]
                    "x" => intermediate_rep.x.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    #[allow(clippy::redundant_clone)]
                    "result" => intermediate_rep.result.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    _ => return std::result::Result::Err("Unexpected key while parsing MinimizeBatchOutput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(MinimizeBatchOutput {
            x: intermediate_rep.x.into_iter().next(),
            result: intermediate_rep.result.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<MinimizeBatchOutput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<MinimizeBatchOutput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<MinimizeBatchOutput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for MinimizeBatchOutput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<MinimizeBatchOutput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <MinimizeBatchOutput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into MinimizeBatchOutput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl MinimizeBatchOutput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct MinimizeStochasticInput {
    #[serde(rename = "x")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub x: Option<Vec<Vec<f64>>>,

    #[serde(rename = "y")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub y: Option<Vec<f64>>,

}

impl MinimizeStochasticInput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> MinimizeStochasticInput {
        MinimizeStochasticInput {
            x: None,
            y: None,
        }
    }
}

/// Converts the MinimizeStochasticInput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for MinimizeStochasticInput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![
            // Skipping x in query parameter serialization


            self.y.as_ref().map(|y| {
                vec![
                    "y".to_string(),
                    y.iter().map(|x| x.to_string()).collect::<Vec<_>>().join(","),
                ].join(",")
            }),

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a MinimizeStochasticInput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for MinimizeStochasticInput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub x: Vec<Vec<Vec<f64>>>,
            pub y: Vec<Vec<f64>>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing MinimizeStochasticInput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    "x" => return std::result::Result::Err("Parsing a container in this style is not supported in MinimizeStochasticInput".to_string()),
                    "y" => return std::result::Result::Err("Parsing a container in this style is not supported in MinimizeStochasticInput".to_string()),
                    _ => return std::result::Result::Err("Unexpected key while parsing MinimizeStochasticInput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(MinimizeStochasticInput {
            x: intermediate_rep.x.into_iter().next(),
            y: intermediate_rep.y.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<MinimizeStochasticInput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<MinimizeStochasticInput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<MinimizeStochasticInput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for MinimizeStochasticInput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<MinimizeStochasticInput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <MinimizeStochasticInput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into MinimizeStochasticInput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl MinimizeStochasticInput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct MinimizeStochasticOutput {
    #[serde(rename = "x")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub x: Option<f64>,

    #[serde(rename = "result")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub result: Option<f64>,

}

impl MinimizeStochasticOutput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> MinimizeStochasticOutput {
        MinimizeStochasticOutput {
            x: None,
            result: None,
        }
    }
}

/// Converts the MinimizeStochasticOutput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for MinimizeStochasticOutput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![

            self.x.as_ref().map(|x| {
                vec![
                    "x".to_string(),
                    x.to_string(),
                ].join(",")
            }),


            self.result.as_ref().map(|result| {
                vec![
                    "result".to_string(),
                    result.to_string(),
                ].join(",")
            }),

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a MinimizeStochasticOutput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for MinimizeStochasticOutput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub x: Vec<f64>,
            pub result: Vec<f64>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing MinimizeStochasticOutput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    #[allow(clippy::redundant_clone)]
                    "x" => intermediate_rep.x.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    #[allow(clippy::redundant_clone)]
                    "result" => intermediate_rep.result.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    _ => return std::result::Result::Err("Unexpected key while parsing MinimizeStochasticOutput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(MinimizeStochasticOutput {
            x: intermediate_rep.x.into_iter().next(),
            result: intermediate_rep.result.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<MinimizeStochasticOutput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<MinimizeStochasticOutput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<MinimizeStochasticOutput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for MinimizeStochasticOutput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<MinimizeStochasticOutput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <MinimizeStochasticOutput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into MinimizeStochasticOutput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl MinimizeStochasticOutput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct ModeInput {
    #[serde(rename = "x")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub x: Option<Vec<f64>>,

}

impl ModeInput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> ModeInput {
        ModeInput {
            x: None,
        }
    }
}

/// Converts the ModeInput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for ModeInput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![

            self.x.as_ref().map(|x| {
                vec![
                    "x".to_string(),
                    x.iter().map(|x| x.to_string()).collect::<Vec<_>>().join(","),
                ].join(",")
            }),

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a ModeInput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for ModeInput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub x: Vec<Vec<f64>>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing ModeInput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    "x" => return std::result::Result::Err("Parsing a container in this style is not supported in ModeInput".to_string()),
                    _ => return std::result::Result::Err("Unexpected key while parsing ModeInput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(ModeInput {
            x: intermediate_rep.x.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<ModeInput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<ModeInput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<ModeInput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for ModeInput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<ModeInput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <ModeInput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into ModeInput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl ModeInput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
#[serde(rename = "Order")]
pub struct Order {
    #[serde(rename = "id")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub id: Option<i64>,

    #[serde(rename = "petId")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub pet_id: Option<i64>,

    #[serde(rename = "quantity")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub quantity: Option<i32>,

    #[serde(rename = "shipDate")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub ship_date: Option<chrono::DateTime::<chrono::Utc>>,

    /// Order Status
    // Note: inline enums are not fully supported by openapi-generator
    #[serde(rename = "status")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub status: Option<String>,

    #[serde(rename = "complete")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub complete: Option<bool>,

}

impl Order {
    #[allow(clippy::new_without_default)]
    pub fn new() -> Order {
        Order {
            id: None,
            pet_id: None,
            quantity: None,
            ship_date: None,
            status: None,
            complete: Some(false),
        }
    }
}

/// Converts the Order value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for Order {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![

            self.id.as_ref().map(|id| {
                vec![
                    "id".to_string(),
                    id.to_string(),
                ].join(",")
            }),


            self.pet_id.as_ref().map(|pet_id| {
                vec![
                    "petId".to_string(),
                    pet_id.to_string(),
                ].join(",")
            }),


            self.quantity.as_ref().map(|quantity| {
                vec![
                    "quantity".to_string(),
                    quantity.to_string(),
                ].join(",")
            }),

            // Skipping shipDate in query parameter serialization


            self.status.as_ref().map(|status| {
                vec![
                    "status".to_string(),
                    status.to_string(),
                ].join(",")
            }),


            self.complete.as_ref().map(|complete| {
                vec![
                    "complete".to_string(),
                    complete.to_string(),
                ].join(",")
            }),

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a Order value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for Order {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub id: Vec<i64>,
            pub pet_id: Vec<i64>,
            pub quantity: Vec<i32>,
            pub ship_date: Vec<chrono::DateTime::<chrono::Utc>>,
            pub status: Vec<String>,
            pub complete: Vec<bool>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing Order".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    #[allow(clippy::redundant_clone)]
                    "id" => intermediate_rep.id.push(<i64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    #[allow(clippy::redundant_clone)]
                    "petId" => intermediate_rep.pet_id.push(<i64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    #[allow(clippy::redundant_clone)]
                    "quantity" => intermediate_rep.quantity.push(<i32 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    #[allow(clippy::redundant_clone)]
                    "shipDate" => intermediate_rep.ship_date.push(<chrono::DateTime::<chrono::Utc> as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    #[allow(clippy::redundant_clone)]
                    "status" => intermediate_rep.status.push(<String as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    #[allow(clippy::redundant_clone)]
                    "complete" => intermediate_rep.complete.push(<bool as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    _ => return std::result::Result::Err("Unexpected key while parsing Order".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(Order {
            id: intermediate_rep.id.into_iter().next(),
            pet_id: intermediate_rep.pet_id.into_iter().next(),
            quantity: intermediate_rep.quantity.into_iter().next(),
            ship_date: intermediate_rep.ship_date.into_iter().next(),
            status: intermediate_rep.status.into_iter().next(),
            complete: intermediate_rep.complete.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<Order> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<Order>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<Order>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for Order - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<Order> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <Order as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into Order - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl Order {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct PartialDifferenceQuotientInput {
    /// vector
    #[serde(rename = "v")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub v: Option<Vec<f64>>,

    #[serde(rename = "i")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub i: Option<serde_json::Value>,

    #[serde(rename = "h")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub h: Option<serde_json::Value>,

}

impl PartialDifferenceQuotientInput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> PartialDifferenceQuotientInput {
        PartialDifferenceQuotientInput {
            v: None,
            i: None,
            h: None,
        }
    }
}

/// Converts the PartialDifferenceQuotientInput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for PartialDifferenceQuotientInput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![

            self.v.as_ref().map(|v| {
                vec![
                    "v".to_string(),
                    v.iter().map(|x| x.to_string()).collect::<Vec<_>>().join(","),
                ].join(",")
            }),

            // Skipping i in query parameter serialization

            // Skipping h in query parameter serialization

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a PartialDifferenceQuotientInput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for PartialDifferenceQuotientInput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub v: Vec<Vec<f64>>,
            pub i: Vec<serde_json::Value>,
            pub h: Vec<serde_json::Value>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing PartialDifferenceQuotientInput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    "v" => return std::result::Result::Err("Parsing a container in this style is not supported in PartialDifferenceQuotientInput".to_string()),
                    #[allow(clippy::redundant_clone)]
                    "i" => intermediate_rep.i.push(<serde_json::Value as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    #[allow(clippy::redundant_clone)]
                    "h" => intermediate_rep.h.push(<serde_json::Value as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    _ => return std::result::Result::Err("Unexpected key while parsing PartialDifferenceQuotientInput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(PartialDifferenceQuotientInput {
            v: intermediate_rep.v.into_iter().next(),
            i: intermediate_rep.i.into_iter().next(),
            h: intermediate_rep.h.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<PartialDifferenceQuotientInput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<PartialDifferenceQuotientInput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<PartialDifferenceQuotientInput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for PartialDifferenceQuotientInput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<PartialDifferenceQuotientInput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <PartialDifferenceQuotientInput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into PartialDifferenceQuotientInput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl PartialDifferenceQuotientInput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct PartialDifferenceQuotientOutput {
    #[serde(rename = "x")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub x: Option<f64>,

    #[serde(rename = "result")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub result: Option<f64>,

}

impl PartialDifferenceQuotientOutput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> PartialDifferenceQuotientOutput {
        PartialDifferenceQuotientOutput {
            x: None,
            result: None,
        }
    }
}

/// Converts the PartialDifferenceQuotientOutput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for PartialDifferenceQuotientOutput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![

            self.x.as_ref().map(|x| {
                vec![
                    "x".to_string(),
                    x.to_string(),
                ].join(",")
            }),


            self.result.as_ref().map(|result| {
                vec![
                    "result".to_string(),
                    result.to_string(),
                ].join(",")
            }),

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a PartialDifferenceQuotientOutput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for PartialDifferenceQuotientOutput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub x: Vec<f64>,
            pub result: Vec<f64>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing PartialDifferenceQuotientOutput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    #[allow(clippy::redundant_clone)]
                    "x" => intermediate_rep.x.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    #[allow(clippy::redundant_clone)]
                    "result" => intermediate_rep.result.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    _ => return std::result::Result::Err("Unexpected key while parsing PartialDifferenceQuotientOutput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(PartialDifferenceQuotientOutput {
            x: intermediate_rep.x.into_iter().next(),
            result: intermediate_rep.result.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<PartialDifferenceQuotientOutput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<PartialDifferenceQuotientOutput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<PartialDifferenceQuotientOutput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for PartialDifferenceQuotientOutput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<PartialDifferenceQuotientOutput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <PartialDifferenceQuotientOutput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into PartialDifferenceQuotientOutput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl PartialDifferenceQuotientOutput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
#[serde(rename = "Pet")]
pub struct Pet {
    #[serde(rename = "id")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub id: Option<i64>,

    #[serde(rename = "category")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub category: Option<models::Category>,

    #[serde(rename = "name")]
    pub name: String,

    #[serde(rename = "photoUrls")]
    pub photo_urls: Vec<String>,

    #[serde(rename = "tags")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub tags: Option<Vec<models::Tag>>,

    /// pet status in the store
    // Note: inline enums are not fully supported by openapi-generator
    #[serde(rename = "status")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub status: Option<String>,

}

impl Pet {
    #[allow(clippy::new_without_default)]
    pub fn new(name: String, photo_urls: Vec<String>, ) -> Pet {
        Pet {
            id: None,
            category: None,
            name,
            photo_urls,
            tags: None,
            status: None,
        }
    }
}

/// Converts the Pet value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for Pet {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![

            self.id.as_ref().map(|id| {
                vec![
                    "id".to_string(),
                    id.to_string(),
                ].join(",")
            }),

            // Skipping category in query parameter serialization


            Some("name".to_string()),
            Some(self.name.to_string()),


            Some("photoUrls".to_string()),
            Some(self.photo_urls.iter().map(|x| x.to_string()).collect::<Vec<_>>().join(",")),

            // Skipping tags in query parameter serialization


            self.status.as_ref().map(|status| {
                vec![
                    "status".to_string(),
                    status.to_string(),
                ].join(",")
            }),

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a Pet value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for Pet {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub id: Vec<i64>,
            pub category: Vec<models::Category>,
            pub name: Vec<String>,
            pub photo_urls: Vec<Vec<String>>,
            pub tags: Vec<Vec<models::Tag>>,
            pub status: Vec<String>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing Pet".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    #[allow(clippy::redundant_clone)]
                    "id" => intermediate_rep.id.push(<i64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    #[allow(clippy::redundant_clone)]
                    "category" => intermediate_rep.category.push(<models::Category as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    #[allow(clippy::redundant_clone)]
                    "name" => intermediate_rep.name.push(<String as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    "photoUrls" => return std::result::Result::Err("Parsing a container in this style is not supported in Pet".to_string()),
                    "tags" => return std::result::Result::Err("Parsing a container in this style is not supported in Pet".to_string()),
                    #[allow(clippy::redundant_clone)]
                    "status" => intermediate_rep.status.push(<String as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    _ => return std::result::Result::Err("Unexpected key while parsing Pet".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(Pet {
            id: intermediate_rep.id.into_iter().next(),
            category: intermediate_rep.category.into_iter().next(),
            name: intermediate_rep.name.into_iter().next().ok_or_else(|| "name missing in Pet".to_string())?,
            photo_urls: intermediate_rep.photo_urls.into_iter().next().ok_or_else(|| "photoUrls missing in Pet".to_string())?,
            tags: intermediate_rep.tags.into_iter().next(),
            status: intermediate_rep.status.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<Pet> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<Pet>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<Pet>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for Pet - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<Pet> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <Pet as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into Pet - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl Pet {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct PrecisionInput {
    /// number of True Positives
    #[serde(rename = "tp")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub tp: Option<f64>,

    /// number of False Positives
    #[serde(rename = "fp")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub fp: Option<f64>,

    /// number of False Negatives
    #[serde(rename = "fn")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub r#fn: Option<f64>,

    /// number of True Negatives
    #[serde(rename = "tn")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub tn: Option<f64>,

}

impl PrecisionInput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> PrecisionInput {
        PrecisionInput {
            tp: None,
            fp: None,
            r#fn: None,
            tn: None,
        }
    }
}

/// Converts the PrecisionInput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for PrecisionInput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![

            self.tp.as_ref().map(|tp| {
                vec![
                    "tp".to_string(),
                    tp.to_string(),
                ].join(",")
            }),


            self.fp.as_ref().map(|fp| {
                vec![
                    "fp".to_string(),
                    fp.to_string(),
                ].join(",")
            }),


            self.r#fn.as_ref().map(|r#fn| {
                vec![
                    "fn".to_string(),
                    r#fn.to_string(),
                ].join(",")
            }),


            self.tn.as_ref().map(|tn| {
                vec![
                    "tn".to_string(),
                    tn.to_string(),
                ].join(",")
            }),

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a PrecisionInput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for PrecisionInput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub tp: Vec<f64>,
            pub fp: Vec<f64>,
            pub r#fn: Vec<f64>,
            pub tn: Vec<f64>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing PrecisionInput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    #[allow(clippy::redundant_clone)]
                    "tp" => intermediate_rep.tp.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    #[allow(clippy::redundant_clone)]
                    "fp" => intermediate_rep.fp.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    #[allow(clippy::redundant_clone)]
                    "fn" => intermediate_rep.r#fn.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    #[allow(clippy::redundant_clone)]
                    "tn" => intermediate_rep.tn.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    _ => return std::result::Result::Err("Unexpected key while parsing PrecisionInput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(PrecisionInput {
            tp: intermediate_rep.tp.into_iter().next(),
            fp: intermediate_rep.fp.into_iter().next(),
            r#fn: intermediate_rep.r#fn.into_iter().next(),
            tn: intermediate_rep.tn.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<PrecisionInput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<PrecisionInput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<PrecisionInput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for PrecisionInput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<PrecisionInput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <PrecisionInput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into PrecisionInput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl PrecisionInput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, PartialOrd, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct PrecisionOutput(f64);

impl std::convert::From<f64> for PrecisionOutput {
    fn from(x: f64) -> Self {
        PrecisionOutput(x)
    }
}

impl std::convert::From<PrecisionOutput> for f64 {
    fn from(x: PrecisionOutput) -> Self {
        x.0
    }
}

impl std::ops::Deref for PrecisionOutput {
    type Target = f64;
    fn deref(&self) -> &f64 {
        &self.0
    }
}

impl std::ops::DerefMut for PrecisionOutput {
    fn deref_mut(&mut self) -> &mut f64 {
        &mut self.0
    }
}


impl PrecisionOutput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct QuantileInput {
    #[serde(rename = "x")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub x: Option<Vec<f64>>,

}

impl QuantileInput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> QuantileInput {
        QuantileInput {
            x: None,
        }
    }
}

/// Converts the QuantileInput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for QuantileInput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![

            self.x.as_ref().map(|x| {
                vec![
                    "x".to_string(),
                    x.iter().map(|x| x.to_string()).collect::<Vec<_>>().join(","),
                ].join(",")
            }),

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a QuantileInput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for QuantileInput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub x: Vec<Vec<f64>>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing QuantileInput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    "x" => return std::result::Result::Err("Parsing a container in this style is not supported in QuantileInput".to_string()),
                    _ => return std::result::Result::Err("Unexpected key while parsing QuantileInput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(QuantileInput {
            x: intermediate_rep.x.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<QuantileInput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<QuantileInput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<QuantileInput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for QuantileInput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<QuantileInput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <QuantileInput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into QuantileInput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl QuantileInput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, PartialOrd, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct QuantileOutput(f64);

impl std::convert::From<f64> for QuantileOutput {
    fn from(x: f64) -> Self {
        QuantileOutput(x)
    }
}

impl std::convert::From<QuantileOutput> for f64 {
    fn from(x: QuantileOutput) -> Self {
        x.0
    }
}

impl std::ops::Deref for QuantileOutput {
    type Target = f64;
    fn deref(&self) -> &f64 {
        &self.0
    }
}

impl std::ops::DerefMut for QuantileOutput {
    fn deref_mut(&mut self) -> &mut f64 {
        &mut self.0
    }
}


impl QuantileOutput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct RecallInput {
    /// number of True Positives
    #[serde(rename = "tp")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub tp: Option<f64>,

    /// number of False Positives
    #[serde(rename = "fp")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub fp: Option<f64>,

    /// number of False Negatives
    #[serde(rename = "fn")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub r#fn: Option<f64>,

    /// number of True Negatives
    #[serde(rename = "tn")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub tn: Option<f64>,

}

impl RecallInput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> RecallInput {
        RecallInput {
            tp: None,
            fp: None,
            r#fn: None,
            tn: None,
        }
    }
}

/// Converts the RecallInput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for RecallInput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![

            self.tp.as_ref().map(|tp| {
                vec![
                    "tp".to_string(),
                    tp.to_string(),
                ].join(",")
            }),


            self.fp.as_ref().map(|fp| {
                vec![
                    "fp".to_string(),
                    fp.to_string(),
                ].join(",")
            }),


            self.r#fn.as_ref().map(|r#fn| {
                vec![
                    "fn".to_string(),
                    r#fn.to_string(),
                ].join(",")
            }),


            self.tn.as_ref().map(|tn| {
                vec![
                    "tn".to_string(),
                    tn.to_string(),
                ].join(",")
            }),

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a RecallInput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for RecallInput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub tp: Vec<f64>,
            pub fp: Vec<f64>,
            pub r#fn: Vec<f64>,
            pub tn: Vec<f64>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing RecallInput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    #[allow(clippy::redundant_clone)]
                    "tp" => intermediate_rep.tp.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    #[allow(clippy::redundant_clone)]
                    "fp" => intermediate_rep.fp.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    #[allow(clippy::redundant_clone)]
                    "fn" => intermediate_rep.r#fn.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    #[allow(clippy::redundant_clone)]
                    "tn" => intermediate_rep.tn.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    _ => return std::result::Result::Err("Unexpected key while parsing RecallInput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(RecallInput {
            tp: intermediate_rep.tp.into_iter().next(),
            fp: intermediate_rep.fp.into_iter().next(),
            r#fn: intermediate_rep.r#fn.into_iter().next(),
            tn: intermediate_rep.tn.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<RecallInput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<RecallInput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<RecallInput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for RecallInput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<RecallInput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <RecallInput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into RecallInput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl RecallInput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, PartialOrd, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct RecallOutput(f64);

impl std::convert::From<f64> for RecallOutput {
    fn from(x: f64) -> Self {
        RecallOutput(x)
    }
}

impl std::convert::From<RecallOutput> for f64 {
    fn from(x: RecallOutput) -> Self {
        x.0
    }
}

impl std::ops::Deref for RecallOutput {
    type Target = f64;
    fn deref(&self) -> &f64 {
        &self.0
    }
}

impl std::ops::DerefMut for RecallOutput {
    fn deref_mut(&mut self) -> &mut f64 {
        &mut self.0
    }
}


impl RecallOutput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct ScalarMultiplyInput {
    #[serde(rename = "c")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub c: Option<f64>,

    #[serde(rename = "mat")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub mat: Option<Vec<Vec<f64>>>,

}

impl ScalarMultiplyInput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> ScalarMultiplyInput {
        ScalarMultiplyInput {
            c: None,
            mat: None,
        }
    }
}

/// Converts the ScalarMultiplyInput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for ScalarMultiplyInput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![

            self.c.as_ref().map(|c| {
                vec![
                    "c".to_string(),
                    c.to_string(),
                ].join(",")
            }),

            // Skipping mat in query parameter serialization

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a ScalarMultiplyInput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for ScalarMultiplyInput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub c: Vec<f64>,
            pub mat: Vec<Vec<Vec<f64>>>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing ScalarMultiplyInput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    #[allow(clippy::redundant_clone)]
                    "c" => intermediate_rep.c.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    "mat" => return std::result::Result::Err("Parsing a container in this style is not supported in ScalarMultiplyInput".to_string()),
                    _ => return std::result::Result::Err("Unexpected key while parsing ScalarMultiplyInput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(ScalarMultiplyInput {
            c: intermediate_rep.c.into_iter().next(),
            mat: intermediate_rep.mat.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<ScalarMultiplyInput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<ScalarMultiplyInput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<ScalarMultiplyInput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for ScalarMultiplyInput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<ScalarMultiplyInput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <ScalarMultiplyInput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into ScalarMultiplyInput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl ScalarMultiplyInput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct ShapeInput {
    #[serde(rename = "mat")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub mat: Option<Vec<Vec<f64>>>,

}

impl ShapeInput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> ShapeInput {
        ShapeInput {
            mat: None,
        }
    }
}

/// Converts the ShapeInput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for ShapeInput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![
            // Skipping mat in query parameter serialization

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a ShapeInput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for ShapeInput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub mat: Vec<Vec<Vec<f64>>>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing ShapeInput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    "mat" => return std::result::Result::Err("Parsing a container in this style is not supported in ShapeInput".to_string()),
                    _ => return std::result::Result::Err("Unexpected key while parsing ShapeInput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(ShapeInput {
            mat: intermediate_rep.mat.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<ShapeInput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<ShapeInput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<ShapeInput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for ShapeInput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<ShapeInput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <ShapeInput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into ShapeInput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl ShapeInput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct ShapeOutput {
    #[serde(rename = "nrows")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub nrows: Option<f64>,

    #[serde(rename = "ncols")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub ncols: Option<f64>,

}

impl ShapeOutput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> ShapeOutput {
        ShapeOutput {
            nrows: None,
            ncols: None,
        }
    }
}

/// Converts the ShapeOutput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for ShapeOutput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![

            self.nrows.as_ref().map(|nrows| {
                vec![
                    "nrows".to_string(),
                    nrows.to_string(),
                ].join(",")
            }),


            self.ncols.as_ref().map(|ncols| {
                vec![
                    "ncols".to_string(),
                    ncols.to_string(),
                ].join(",")
            }),

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a ShapeOutput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for ShapeOutput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub nrows: Vec<f64>,
            pub ncols: Vec<f64>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing ShapeOutput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    #[allow(clippy::redundant_clone)]
                    "nrows" => intermediate_rep.nrows.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    #[allow(clippy::redundant_clone)]
                    "ncols" => intermediate_rep.ncols.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    _ => return std::result::Result::Err("Unexpected key while parsing ShapeOutput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(ShapeOutput {
            nrows: intermediate_rep.nrows.into_iter().next(),
            ncols: intermediate_rep.ncols.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<ShapeOutput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<ShapeOutput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<ShapeOutput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for ShapeOutput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<ShapeOutput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <ShapeOutput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into ShapeOutput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl ShapeOutput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct SplitDataInput {
    #[serde(rename = "data")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub data: Option<Vec<Vec<f64>>>,

}

impl SplitDataInput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> SplitDataInput {
        SplitDataInput {
            data: None,
        }
    }
}

/// Converts the SplitDataInput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for SplitDataInput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![
            // Skipping data in query parameter serialization

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a SplitDataInput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for SplitDataInput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub data: Vec<Vec<Vec<f64>>>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing SplitDataInput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    "data" => return std::result::Result::Err("Parsing a container in this style is not supported in SplitDataInput".to_string()),
                    _ => return std::result::Result::Err("Unexpected key while parsing SplitDataInput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(SplitDataInput {
            data: intermediate_rep.data.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<SplitDataInput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<SplitDataInput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<SplitDataInput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for SplitDataInput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<SplitDataInput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <SplitDataInput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into SplitDataInput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl SplitDataInput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct SplitDataOutput {
    #[serde(rename = "train")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub train: Option<Vec<Vec<f64>>>,

    #[serde(rename = "test")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub test: Option<Vec<Vec<f64>>>,

}

impl SplitDataOutput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> SplitDataOutput {
        SplitDataOutput {
            train: None,
            test: None,
        }
    }
}

/// Converts the SplitDataOutput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for SplitDataOutput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![
            // Skipping train in query parameter serialization

            // Skipping test in query parameter serialization

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a SplitDataOutput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for SplitDataOutput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub train: Vec<Vec<Vec<f64>>>,
            pub test: Vec<Vec<Vec<f64>>>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing SplitDataOutput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    "train" => return std::result::Result::Err("Parsing a container in this style is not supported in SplitDataOutput".to_string()),
                    "test" => return std::result::Result::Err("Parsing a container in this style is not supported in SplitDataOutput".to_string()),
                    _ => return std::result::Result::Err("Unexpected key while parsing SplitDataOutput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(SplitDataOutput {
            train: intermediate_rep.train.into_iter().next(),
            test: intermediate_rep.test.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<SplitDataOutput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<SplitDataOutput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<SplitDataOutput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for SplitDataOutput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<SplitDataOutput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <SplitDataOutput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into SplitDataOutput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl SplitDataOutput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct SqrtInput {
    #[serde(rename = "x")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub x: Option<f64>,

}

impl SqrtInput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> SqrtInput {
        SqrtInput {
            x: None,
        }
    }
}

/// Converts the SqrtInput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for SqrtInput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![

            self.x.as_ref().map(|x| {
                vec![
                    "x".to_string(),
                    x.to_string(),
                ].join(",")
            }),

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a SqrtInput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for SqrtInput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub x: Vec<f64>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing SqrtInput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    #[allow(clippy::redundant_clone)]
                    "x" => intermediate_rep.x.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    _ => return std::result::Result::Err("Unexpected key while parsing SqrtInput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(SqrtInput {
            x: intermediate_rep.x.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<SqrtInput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<SqrtInput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<SqrtInput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for SqrtInput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<SqrtInput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <SqrtInput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into SqrtInput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl SqrtInput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct SqrtOutput {
    #[serde(rename = "x")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub x: Option<f64>,

    #[serde(rename = "result")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub result: Option<f64>,

}

impl SqrtOutput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> SqrtOutput {
        SqrtOutput {
            x: None,
            result: None,
        }
    }
}

/// Converts the SqrtOutput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for SqrtOutput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![

            self.x.as_ref().map(|x| {
                vec![
                    "x".to_string(),
                    x.to_string(),
                ].join(",")
            }),


            self.result.as_ref().map(|result| {
                vec![
                    "result".to_string(),
                    result.to_string(),
                ].join(",")
            }),

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a SqrtOutput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for SqrtOutput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub x: Vec<f64>,
            pub result: Vec<f64>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing SqrtOutput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    #[allow(clippy::redundant_clone)]
                    "x" => intermediate_rep.x.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    #[allow(clippy::redundant_clone)]
                    "result" => intermediate_rep.result.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    _ => return std::result::Result::Err("Unexpected key while parsing SqrtOutput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(SqrtOutput {
            x: intermediate_rep.x.into_iter().next(),
            result: intermediate_rep.result.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<SqrtOutput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<SqrtOutput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<SqrtOutput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for SqrtOutput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<SqrtOutput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <SqrtOutput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into SqrtOutput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl SqrtOutput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct SquaredDistanceInput {
    #[serde(rename = "v")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub v: Option<Vec<f64>>,

    #[serde(rename = "w")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub w: Option<Vec<f64>>,

}

impl SquaredDistanceInput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> SquaredDistanceInput {
        SquaredDistanceInput {
            v: None,
            w: None,
        }
    }
}

/// Converts the SquaredDistanceInput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for SquaredDistanceInput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![

            self.v.as_ref().map(|v| {
                vec![
                    "v".to_string(),
                    v.iter().map(|x| x.to_string()).collect::<Vec<_>>().join(","),
                ].join(",")
            }),


            self.w.as_ref().map(|w| {
                vec![
                    "w".to_string(),
                    w.iter().map(|x| x.to_string()).collect::<Vec<_>>().join(","),
                ].join(",")
            }),

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a SquaredDistanceInput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for SquaredDistanceInput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub v: Vec<Vec<f64>>,
            pub w: Vec<Vec<f64>>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing SquaredDistanceInput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    "v" => return std::result::Result::Err("Parsing a container in this style is not supported in SquaredDistanceInput".to_string()),
                    "w" => return std::result::Result::Err("Parsing a container in this style is not supported in SquaredDistanceInput".to_string()),
                    _ => return std::result::Result::Err("Unexpected key while parsing SquaredDistanceInput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(SquaredDistanceInput {
            v: intermediate_rep.v.into_iter().next(),
            w: intermediate_rep.w.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<SquaredDistanceInput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<SquaredDistanceInput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<SquaredDistanceInput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for SquaredDistanceInput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<SquaredDistanceInput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <SquaredDistanceInput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into SquaredDistanceInput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl SquaredDistanceInput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct StandardDeviationInput {
    #[serde(rename = "x")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub x: Option<Vec<f64>>,

}

impl StandardDeviationInput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> StandardDeviationInput {
        StandardDeviationInput {
            x: None,
        }
    }
}

/// Converts the StandardDeviationInput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for StandardDeviationInput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![

            self.x.as_ref().map(|x| {
                vec![
                    "x".to_string(),
                    x.iter().map(|x| x.to_string()).collect::<Vec<_>>().join(","),
                ].join(",")
            }),

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a StandardDeviationInput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for StandardDeviationInput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub x: Vec<Vec<f64>>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing StandardDeviationInput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    "x" => return std::result::Result::Err("Parsing a container in this style is not supported in StandardDeviationInput".to_string()),
                    _ => return std::result::Result::Err("Unexpected key while parsing StandardDeviationInput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(StandardDeviationInput {
            x: intermediate_rep.x.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<StandardDeviationInput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<StandardDeviationInput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<StandardDeviationInput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for StandardDeviationInput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<StandardDeviationInput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <StandardDeviationInput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into StandardDeviationInput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl StandardDeviationInput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, PartialOrd, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct StandardDeviationOutput(f64);

impl std::convert::From<f64> for StandardDeviationOutput {
    fn from(x: f64) -> Self {
        StandardDeviationOutput(x)
    }
}

impl std::convert::From<StandardDeviationOutput> for f64 {
    fn from(x: StandardDeviationOutput) -> Self {
        x.0
    }
}

impl std::ops::Deref for StandardDeviationOutput {
    type Target = f64;
    fn deref(&self) -> &f64 {
        &self.0
    }
}

impl std::ops::DerefMut for StandardDeviationOutput {
    fn deref_mut(&mut self) -> &mut f64 {
        &mut self.0
    }
}


impl StandardDeviationOutput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct StrengthInput {
    #[serde(rename = "actual")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub actual: Option<i32>,

    #[serde(rename = "expected")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub expected: Option<i32>,

}

impl StrengthInput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> StrengthInput {
        StrengthInput {
            actual: None,
            expected: None,
        }
    }
}

/// Converts the StrengthInput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for StrengthInput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![

            self.actual.as_ref().map(|actual| {
                vec![
                    "actual".to_string(),
                    actual.to_string(),
                ].join(",")
            }),


            self.expected.as_ref().map(|expected| {
                vec![
                    "expected".to_string(),
                    expected.to_string(),
                ].join(",")
            }),

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a StrengthInput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for StrengthInput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub actual: Vec<i32>,
            pub expected: Vec<i32>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing StrengthInput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    #[allow(clippy::redundant_clone)]
                    "actual" => intermediate_rep.actual.push(<i32 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    #[allow(clippy::redundant_clone)]
                    "expected" => intermediate_rep.expected.push(<i32 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    _ => return std::result::Result::Err("Unexpected key while parsing StrengthInput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(StrengthInput {
            actual: intermediate_rep.actual.into_iter().next(),
            expected: intermediate_rep.expected.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<StrengthInput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<StrengthInput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<StrengthInput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for StrengthInput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<StrengthInput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <StrengthInput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into StrengthInput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl StrengthInput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct StrengthOutput {
    #[serde(rename = "actual")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub actual: Option<i32>,

    #[serde(rename = "expected")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub expected: Option<i32>,

    #[serde(rename = "strength")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub strength: Option<f64>,

}

impl StrengthOutput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> StrengthOutput {
        StrengthOutput {
            actual: None,
            expected: None,
            strength: None,
        }
    }
}

/// Converts the StrengthOutput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for StrengthOutput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![

            self.actual.as_ref().map(|actual| {
                vec![
                    "actual".to_string(),
                    actual.to_string(),
                ].join(",")
            }),


            self.expected.as_ref().map(|expected| {
                vec![
                    "expected".to_string(),
                    expected.to_string(),
                ].join(",")
            }),


            self.strength.as_ref().map(|strength| {
                vec![
                    "strength".to_string(),
                    strength.to_string(),
                ].join(",")
            }),

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a StrengthOutput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for StrengthOutput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub actual: Vec<i32>,
            pub expected: Vec<i32>,
            pub strength: Vec<f64>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing StrengthOutput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    #[allow(clippy::redundant_clone)]
                    "actual" => intermediate_rep.actual.push(<i32 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    #[allow(clippy::redundant_clone)]
                    "expected" => intermediate_rep.expected.push(<i32 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    #[allow(clippy::redundant_clone)]
                    "strength" => intermediate_rep.strength.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    _ => return std::result::Result::Err("Unexpected key while parsing StrengthOutput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(StrengthOutput {
            actual: intermediate_rep.actual.into_iter().next(),
            expected: intermediate_rep.expected.into_iter().next(),
            strength: intermediate_rep.strength.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<StrengthOutput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<StrengthOutput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<StrengthOutput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for StrengthOutput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<StrengthOutput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <StrengthOutput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into StrengthOutput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl StrengthOutput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct SumOfSquaresInput {
    #[serde(rename = "x")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub x: Option<Vec<f64>>,

}

impl SumOfSquaresInput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> SumOfSquaresInput {
        SumOfSquaresInput {
            x: None,
        }
    }
}

/// Converts the SumOfSquaresInput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for SumOfSquaresInput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![

            self.x.as_ref().map(|x| {
                vec![
                    "x".to_string(),
                    x.iter().map(|x| x.to_string()).collect::<Vec<_>>().join(","),
                ].join(",")
            }),

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a SumOfSquaresInput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for SumOfSquaresInput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub x: Vec<Vec<f64>>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing SumOfSquaresInput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    "x" => return std::result::Result::Err("Parsing a container in this style is not supported in SumOfSquaresInput".to_string()),
                    _ => return std::result::Result::Err("Unexpected key while parsing SumOfSquaresInput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(SumOfSquaresInput {
            x: intermediate_rep.x.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<SumOfSquaresInput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<SumOfSquaresInput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<SumOfSquaresInput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for SumOfSquaresInput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<SumOfSquaresInput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <SumOfSquaresInput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into SumOfSquaresInput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl SumOfSquaresInput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, PartialOrd, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct SumOfSquaresOutput(f64);

impl std::convert::From<f64> for SumOfSquaresOutput {
    fn from(x: f64) -> Self {
        SumOfSquaresOutput(x)
    }
}

impl std::convert::From<SumOfSquaresOutput> for f64 {
    fn from(x: SumOfSquaresOutput) -> Self {
        x.0
    }
}

impl std::ops::Deref for SumOfSquaresOutput {
    type Target = f64;
    fn deref(&self) -> &f64 {
        &self.0
    }
}

impl std::ops::DerefMut for SumOfSquaresOutput {
    fn deref_mut(&mut self) -> &mut f64 {
        &mut self.0
    }
}


impl SumOfSquaresOutput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
#[serde(rename = "Tag")]
pub struct Tag {
    #[serde(rename = "id")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub id: Option<i64>,

    #[serde(rename = "name")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub name: Option<String>,

}

impl Tag {
    #[allow(clippy::new_without_default)]
    pub fn new() -> Tag {
        Tag {
            id: None,
            name: None,
        }
    }
}

/// Converts the Tag value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for Tag {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![

            self.id.as_ref().map(|id| {
                vec![
                    "id".to_string(),
                    id.to_string(),
                ].join(",")
            }),


            self.name.as_ref().map(|name| {
                vec![
                    "name".to_string(),
                    name.to_string(),
                ].join(",")
            }),

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a Tag value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for Tag {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub id: Vec<i64>,
            pub name: Vec<String>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing Tag".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    #[allow(clippy::redundant_clone)]
                    "id" => intermediate_rep.id.push(<i64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    #[allow(clippy::redundant_clone)]
                    "name" => intermediate_rep.name.push(<String as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    _ => return std::result::Result::Err("Unexpected key while parsing Tag".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(Tag {
            id: intermediate_rep.id.into_iter().next(),
            name: intermediate_rep.name.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<Tag> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<Tag>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<Tag>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for Tag - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<Tag> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <Tag as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into Tag - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl Tag {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct TrainTestSplitInput {
    #[serde(rename = "x")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub x: Option<Vec<Vec<f64>>>,

    #[serde(rename = "y")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub y: Option<Vec<Vec<f64>>>,

    #[serde(rename = "p")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub p: Option<f64>,

}

impl TrainTestSplitInput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> TrainTestSplitInput {
        TrainTestSplitInput {
            x: None,
            y: None,
            p: None,
        }
    }
}

/// Converts the TrainTestSplitInput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for TrainTestSplitInput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![
            // Skipping x in query parameter serialization

            // Skipping y in query parameter serialization


            self.p.as_ref().map(|p| {
                vec![
                    "p".to_string(),
                    p.to_string(),
                ].join(",")
            }),

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a TrainTestSplitInput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for TrainTestSplitInput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub x: Vec<Vec<Vec<f64>>>,
            pub y: Vec<Vec<Vec<f64>>>,
            pub p: Vec<f64>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing TrainTestSplitInput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    "x" => return std::result::Result::Err("Parsing a container in this style is not supported in TrainTestSplitInput".to_string()),
                    "y" => return std::result::Result::Err("Parsing a container in this style is not supported in TrainTestSplitInput".to_string()),
                    #[allow(clippy::redundant_clone)]
                    "p" => intermediate_rep.p.push(<f64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    _ => return std::result::Result::Err("Unexpected key while parsing TrainTestSplitInput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(TrainTestSplitInput {
            x: intermediate_rep.x.into_iter().next(),
            y: intermediate_rep.y.into_iter().next(),
            p: intermediate_rep.p.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<TrainTestSplitInput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<TrainTestSplitInput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<TrainTestSplitInput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for TrainTestSplitInput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<TrainTestSplitInput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <TrainTestSplitInput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into TrainTestSplitInput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl TrainTestSplitInput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct TrainTestSplitOutput {
    #[serde(rename = "x_train")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub x_train: Option<Vec<Vec<f64>>>,

    #[serde(rename = "x_test")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub x_test: Option<Vec<Vec<f64>>>,

    #[serde(rename = "y_train")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub y_train: Option<Vec<f64>>,

    #[serde(rename = "y_test")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub y_test: Option<Vec<f64>>,

}

impl TrainTestSplitOutput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> TrainTestSplitOutput {
        TrainTestSplitOutput {
            x_train: None,
            x_test: None,
            y_train: None,
            y_test: None,
        }
    }
}

/// Converts the TrainTestSplitOutput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for TrainTestSplitOutput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![
            // Skipping x_train in query parameter serialization

            // Skipping x_test in query parameter serialization


            self.y_train.as_ref().map(|y_train| {
                vec![
                    "y_train".to_string(),
                    y_train.iter().map(|x| x.to_string()).collect::<Vec<_>>().join(","),
                ].join(",")
            }),


            self.y_test.as_ref().map(|y_test| {
                vec![
                    "y_test".to_string(),
                    y_test.iter().map(|x| x.to_string()).collect::<Vec<_>>().join(","),
                ].join(",")
            }),

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a TrainTestSplitOutput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for TrainTestSplitOutput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub x_train: Vec<Vec<Vec<f64>>>,
            pub x_test: Vec<Vec<Vec<f64>>>,
            pub y_train: Vec<Vec<f64>>,
            pub y_test: Vec<Vec<f64>>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing TrainTestSplitOutput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    "x_train" => return std::result::Result::Err("Parsing a container in this style is not supported in TrainTestSplitOutput".to_string()),
                    "x_test" => return std::result::Result::Err("Parsing a container in this style is not supported in TrainTestSplitOutput".to_string()),
                    "y_train" => return std::result::Result::Err("Parsing a container in this style is not supported in TrainTestSplitOutput".to_string()),
                    "y_test" => return std::result::Result::Err("Parsing a container in this style is not supported in TrainTestSplitOutput".to_string()),
                    _ => return std::result::Result::Err("Unexpected key while parsing TrainTestSplitOutput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(TrainTestSplitOutput {
            x_train: intermediate_rep.x_train.into_iter().next(),
            x_test: intermediate_rep.x_test.into_iter().next(),
            y_train: intermediate_rep.y_train.into_iter().next(),
            y_test: intermediate_rep.y_test.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<TrainTestSplitOutput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<TrainTestSplitOutput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<TrainTestSplitOutput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for TrainTestSplitOutput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<TrainTestSplitOutput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <TrainTestSplitOutput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into TrainTestSplitOutput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl TrainTestSplitOutput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
#[serde(rename = "User")]
pub struct User {
    #[serde(rename = "id")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub id: Option<i64>,

    #[serde(rename = "username")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub username: Option<String>,

    #[serde(rename = "firstName")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub first_name: Option<String>,

    #[serde(rename = "lastName")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub last_name: Option<String>,

    #[serde(rename = "email")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub email: Option<String>,

    #[serde(rename = "password")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub password: Option<String>,

    #[serde(rename = "phone")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub phone: Option<String>,

    /// User Status
    #[serde(rename = "userStatus")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub user_status: Option<i32>,

}

impl User {
    #[allow(clippy::new_without_default)]
    pub fn new() -> User {
        User {
            id: None,
            username: None,
            first_name: None,
            last_name: None,
            email: None,
            password: None,
            phone: None,
            user_status: None,
        }
    }
}

/// Converts the User value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for User {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![

            self.id.as_ref().map(|id| {
                vec![
                    "id".to_string(),
                    id.to_string(),
                ].join(",")
            }),


            self.username.as_ref().map(|username| {
                vec![
                    "username".to_string(),
                    username.to_string(),
                ].join(",")
            }),


            self.first_name.as_ref().map(|first_name| {
                vec![
                    "firstName".to_string(),
                    first_name.to_string(),
                ].join(",")
            }),


            self.last_name.as_ref().map(|last_name| {
                vec![
                    "lastName".to_string(),
                    last_name.to_string(),
                ].join(",")
            }),


            self.email.as_ref().map(|email| {
                vec![
                    "email".to_string(),
                    email.to_string(),
                ].join(",")
            }),


            self.password.as_ref().map(|password| {
                vec![
                    "password".to_string(),
                    password.to_string(),
                ].join(",")
            }),


            self.phone.as_ref().map(|phone| {
                vec![
                    "phone".to_string(),
                    phone.to_string(),
                ].join(",")
            }),


            self.user_status.as_ref().map(|user_status| {
                vec![
                    "userStatus".to_string(),
                    user_status.to_string(),
                ].join(",")
            }),

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a User value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for User {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub id: Vec<i64>,
            pub username: Vec<String>,
            pub first_name: Vec<String>,
            pub last_name: Vec<String>,
            pub email: Vec<String>,
            pub password: Vec<String>,
            pub phone: Vec<String>,
            pub user_status: Vec<i32>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing User".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    #[allow(clippy::redundant_clone)]
                    "id" => intermediate_rep.id.push(<i64 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    #[allow(clippy::redundant_clone)]
                    "username" => intermediate_rep.username.push(<String as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    #[allow(clippy::redundant_clone)]
                    "firstName" => intermediate_rep.first_name.push(<String as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    #[allow(clippy::redundant_clone)]
                    "lastName" => intermediate_rep.last_name.push(<String as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    #[allow(clippy::redundant_clone)]
                    "email" => intermediate_rep.email.push(<String as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    #[allow(clippy::redundant_clone)]
                    "password" => intermediate_rep.password.push(<String as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    #[allow(clippy::redundant_clone)]
                    "phone" => intermediate_rep.phone.push(<String as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    #[allow(clippy::redundant_clone)]
                    "userStatus" => intermediate_rep.user_status.push(<i32 as std::str::FromStr>::from_str(val).map_err(|x| x.to_string())?),
                    _ => return std::result::Result::Err("Unexpected key while parsing User".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(User {
            id: intermediate_rep.id.into_iter().next(),
            username: intermediate_rep.username.into_iter().next(),
            first_name: intermediate_rep.first_name.into_iter().next(),
            last_name: intermediate_rep.last_name.into_iter().next(),
            email: intermediate_rep.email.into_iter().next(),
            password: intermediate_rep.password.into_iter().next(),
            phone: intermediate_rep.phone.into_iter().next(),
            user_status: intermediate_rep.user_status.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<User> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<User>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<User>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for User - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<User> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <User as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into User - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl User {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct VarianceInput {
    #[serde(rename = "x")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub x: Option<Vec<f64>>,

}

impl VarianceInput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> VarianceInput {
        VarianceInput {
            x: None,
        }
    }
}

/// Converts the VarianceInput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for VarianceInput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![

            self.x.as_ref().map(|x| {
                vec![
                    "x".to_string(),
                    x.iter().map(|x| x.to_string()).collect::<Vec<_>>().join(","),
                ].join(",")
            }),

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a VarianceInput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for VarianceInput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub x: Vec<Vec<f64>>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing VarianceInput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    "x" => return std::result::Result::Err("Parsing a container in this style is not supported in VarianceInput".to_string()),
                    _ => return std::result::Result::Err("Unexpected key while parsing VarianceInput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(VarianceInput {
            x: intermediate_rep.x.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<VarianceInput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<VarianceInput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<VarianceInput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for VarianceInput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<VarianceInput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <VarianceInput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into VarianceInput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl VarianceInput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, PartialOrd, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct VarianceOutput(f64);

impl std::convert::From<f64> for VarianceOutput {
    fn from(x: f64) -> Self {
        VarianceOutput(x)
    }
}

impl std::convert::From<VarianceOutput> for f64 {
    fn from(x: VarianceOutput) -> Self {
        x.0
    }
}

impl std::ops::Deref for VarianceOutput {
    type Target = f64;
    fn deref(&self) -> &f64 {
        &self.0
    }
}

impl std::ops::DerefMut for VarianceOutput {
    fn deref_mut(&mut self) -> &mut f64 {
        &mut self.0
    }
}


impl VarianceOutput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct VectorAddInput {
    #[serde(rename = "v")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub v: Option<Vec<f64>>,

    #[serde(rename = "w")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub w: Option<Vec<f64>>,

}

impl VectorAddInput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> VectorAddInput {
        VectorAddInput {
            v: None,
            w: None,
        }
    }
}

/// Converts the VectorAddInput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for VectorAddInput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![

            self.v.as_ref().map(|v| {
                vec![
                    "v".to_string(),
                    v.iter().map(|x| x.to_string()).collect::<Vec<_>>().join(","),
                ].join(",")
            }),


            self.w.as_ref().map(|w| {
                vec![
                    "w".to_string(),
                    w.iter().map(|x| x.to_string()).collect::<Vec<_>>().join(","),
                ].join(",")
            }),

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a VectorAddInput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for VectorAddInput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub v: Vec<Vec<f64>>,
            pub w: Vec<Vec<f64>>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing VectorAddInput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    "v" => return std::result::Result::Err("Parsing a container in this style is not supported in VectorAddInput".to_string()),
                    "w" => return std::result::Result::Err("Parsing a container in this style is not supported in VectorAddInput".to_string()),
                    _ => return std::result::Result::Err("Unexpected key while parsing VectorAddInput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(VectorAddInput {
            v: intermediate_rep.v.into_iter().next(),
            w: intermediate_rep.w.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<VectorAddInput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<VectorAddInput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<VectorAddInput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for VectorAddInput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<VectorAddInput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <VectorAddInput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into VectorAddInput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl VectorAddInput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct VectorMeanInput {
    #[serde(rename = "v")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub v: Option<Vec<f64>>,

    #[serde(rename = "w")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub w: Option<Vec<f64>>,

}

impl VectorMeanInput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> VectorMeanInput {
        VectorMeanInput {
            v: None,
            w: None,
        }
    }
}

/// Converts the VectorMeanInput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for VectorMeanInput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![

            self.v.as_ref().map(|v| {
                vec![
                    "v".to_string(),
                    v.iter().map(|x| x.to_string()).collect::<Vec<_>>().join(","),
                ].join(",")
            }),


            self.w.as_ref().map(|w| {
                vec![
                    "w".to_string(),
                    w.iter().map(|x| x.to_string()).collect::<Vec<_>>().join(","),
                ].join(",")
            }),

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a VectorMeanInput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for VectorMeanInput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub v: Vec<Vec<f64>>,
            pub w: Vec<Vec<f64>>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing VectorMeanInput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    "v" => return std::result::Result::Err("Parsing a container in this style is not supported in VectorMeanInput".to_string()),
                    "w" => return std::result::Result::Err("Parsing a container in this style is not supported in VectorMeanInput".to_string()),
                    _ => return std::result::Result::Err("Unexpected key while parsing VectorMeanInput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(VectorMeanInput {
            v: intermediate_rep.v.into_iter().next(),
            w: intermediate_rep.w.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<VectorMeanInput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<VectorMeanInput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<VectorMeanInput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for VectorMeanInput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<VectorMeanInput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <VectorMeanInput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into VectorMeanInput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl VectorMeanInput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct VectorSubtractInput {
    #[serde(rename = "v")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub v: Option<Vec<f64>>,

    #[serde(rename = "w")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub w: Option<Vec<f64>>,

}

impl VectorSubtractInput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> VectorSubtractInput {
        VectorSubtractInput {
            v: None,
            w: None,
        }
    }
}

/// Converts the VectorSubtractInput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for VectorSubtractInput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![

            self.v.as_ref().map(|v| {
                vec![
                    "v".to_string(),
                    v.iter().map(|x| x.to_string()).collect::<Vec<_>>().join(","),
                ].join(",")
            }),


            self.w.as_ref().map(|w| {
                vec![
                    "w".to_string(),
                    w.iter().map(|x| x.to_string()).collect::<Vec<_>>().join(","),
                ].join(",")
            }),

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a VectorSubtractInput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for VectorSubtractInput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub v: Vec<Vec<f64>>,
            pub w: Vec<Vec<f64>>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing VectorSubtractInput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    "v" => return std::result::Result::Err("Parsing a container in this style is not supported in VectorSubtractInput".to_string()),
                    "w" => return std::result::Result::Err("Parsing a container in this style is not supported in VectorSubtractInput".to_string()),
                    _ => return std::result::Result::Err("Unexpected key while parsing VectorSubtractInput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(VectorSubtractInput {
            v: intermediate_rep.v.into_iter().next(),
            w: intermediate_rep.w.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<VectorSubtractInput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<VectorSubtractInput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<VectorSubtractInput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for VectorSubtractInput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<VectorSubtractInput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <VectorSubtractInput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into VectorSubtractInput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl VectorSubtractInput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}

#[derive(Debug, Clone, PartialEq, serde::Serialize, serde::Deserialize)]
#[cfg_attr(feature = "conversion", derive(frunk::LabelledGeneric))]
pub struct VectorSumInput {
    #[serde(rename = "v")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub v: Option<Vec<f64>>,

    #[serde(rename = "w")]
    #[serde(skip_serializing_if="Option::is_none")]
    pub w: Option<Vec<f64>>,

}

impl VectorSumInput {
    #[allow(clippy::new_without_default)]
    pub fn new() -> VectorSumInput {
        VectorSumInput {
            v: None,
            w: None,
        }
    }
}

/// Converts the VectorSumInput value to the Query Parameters representation (style=form, explode=false)
/// specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde serializer
impl std::string::ToString for VectorSumInput {
    fn to_string(&self) -> String {
        let params: Vec<Option<String>> = vec![

            self.v.as_ref().map(|v| {
                vec![
                    "v".to_string(),
                    v.iter().map(|x| x.to_string()).collect::<Vec<_>>().join(","),
                ].join(",")
            }),


            self.w.as_ref().map(|w| {
                vec![
                    "w".to_string(),
                    w.iter().map(|x| x.to_string()).collect::<Vec<_>>().join(","),
                ].join(",")
            }),

        ];

        params.into_iter().flatten().collect::<Vec<_>>().join(",")
    }
}

/// Converts Query Parameters representation (style=form, explode=false) to a VectorSumInput value
/// as specified in https://swagger.io/docs/specification/serialization/
/// Should be implemented in a serde deserializer
impl std::str::FromStr for VectorSumInput {
    type Err = String;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        /// An intermediate representation of the struct to use for parsing.
        #[derive(Default)]
        #[allow(dead_code)]
        struct IntermediateRep {
            pub v: Vec<Vec<f64>>,
            pub w: Vec<Vec<f64>>,
        }

        let mut intermediate_rep = IntermediateRep::default();

        // Parse into intermediate representation
        let mut string_iter = s.split(',');
        let mut key_result = string_iter.next();

        while key_result.is_some() {
            let val = match string_iter.next() {
                Some(x) => x,
                None => return std::result::Result::Err("Missing value while parsing VectorSumInput".to_string())
            };

            if let Some(key) = key_result {
                #[allow(clippy::match_single_binding)]
                match key {
                    "v" => return std::result::Result::Err("Parsing a container in this style is not supported in VectorSumInput".to_string()),
                    "w" => return std::result::Result::Err("Parsing a container in this style is not supported in VectorSumInput".to_string()),
                    _ => return std::result::Result::Err("Unexpected key while parsing VectorSumInput".to_string())
                }
            }

            // Get the next key
            key_result = string_iter.next();
        }

        // Use the intermediate representation to return the struct
        std::result::Result::Ok(VectorSumInput {
            v: intermediate_rep.v.into_iter().next(),
            w: intermediate_rep.w.into_iter().next(),
        })
    }
}

// Methods for converting between header::IntoHeaderValue<VectorSumInput> and hyper::header::HeaderValue

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<header::IntoHeaderValue<VectorSumInput>> for hyper::header::HeaderValue {
    type Error = String;

    fn try_from(hdr_value: header::IntoHeaderValue<VectorSumInput>) -> std::result::Result<Self, Self::Error> {
        let hdr_value = hdr_value.to_string();
        match hyper::header::HeaderValue::from_str(&hdr_value) {
             std::result::Result::Ok(value) => std::result::Result::Ok(value),
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Invalid header value for VectorSumInput - value: {} is invalid {}",
                     hdr_value, e))
        }
    }
}

#[cfg(any(feature = "client", feature = "server"))]
impl std::convert::TryFrom<hyper::header::HeaderValue> for header::IntoHeaderValue<VectorSumInput> {
    type Error = String;

    fn try_from(hdr_value: hyper::header::HeaderValue) -> std::result::Result<Self, Self::Error> {
        match hdr_value.to_str() {
             std::result::Result::Ok(value) => {
                    match <VectorSumInput as std::str::FromStr>::from_str(value) {
                        std::result::Result::Ok(value) => std::result::Result::Ok(header::IntoHeaderValue(value)),
                        std::result::Result::Err(err) => std::result::Result::Err(
                            format!("Unable to convert header value '{}' into VectorSumInput - {}",
                                value, err))
                    }
             },
             std::result::Result::Err(e) => std::result::Result::Err(
                 format!("Unable to convert header: {:?} to string: {}",
                     hdr_value, e))
        }
    }
}


impl VectorSumInput {
    /// Helper function to allow us to convert this model to an XML string.
    /// Will panic if serialisation fails.
    #[allow(dead_code)]
    pub(crate) fn as_xml(&self) -> String {
        serde_xml_rs::to_string(&self).expect("impossible to fail to serialize")
    }
}
