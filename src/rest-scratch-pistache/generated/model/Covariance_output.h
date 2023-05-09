/**
* Minimal Pistache
* This is a sample server
*
* The version of the OpenAPI document: 1.0.0
* 
*
* NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
* https://openapi-generator.tech
* Do not edit the class manually.
*/
/*
 * Covariance_output.h
 *
 * 
 */

#ifndef Covariance_output_H_
#define Covariance_output_H_


#include <nlohmann/json.hpp>

namespace org::openapitools::server::model
{

/// <summary>
/// 
/// </summary>
class  Covariance_output
{
public:
    Covariance_output();
    virtual ~Covariance_output() = default;


    /// <summary>
    /// Validate the current data in the model. Throws a ValidationException on failure.
    /// </summary>
    void validate() const;

    /// <summary>
    /// Validate the current data in the model. Returns false on error and writes an error
    /// message into the given stringstream.
    /// </summary>
    bool validate(std::stringstream& msg) const;

    /// <summary>
    /// Helper overload for validate. Used when one model stores another model and calls it's validate.
    /// Not meant to be called outside that case.
    /// </summary>
    bool validate(std::stringstream& msg, const std::string& pathPrefix) const;

    bool operator==(const Covariance_output& rhs) const;
    bool operator!=(const Covariance_output& rhs) const;

    /////////////////////////////////////////////
    /// Covariance_output members

    /// <summary>
    /// 
    /// </summary>
    double getX() const;
    void setX(double const value);
    bool XIsSet() const;
    void unsetx();
    /// <summary>
    /// 
    /// </summary>
    double getResult() const;
    void setResult(double const value);
    bool resultIsSet() const;
    void unsetResult();

    friend void to_json(nlohmann::json& j, const Covariance_output& o);
    friend void from_json(const nlohmann::json& j, Covariance_output& o);
protected:
    double m_x;
    bool m_xIsSet;
    double m_Result;
    bool m_ResultIsSet;
    
};

} // namespace org::openapitools::server::model

#endif /* Covariance_output_H_ */
