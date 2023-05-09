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
 * Magnitude_input.h
 *
 * 
 */

#ifndef Magnitude_input_H_
#define Magnitude_input_H_


#include <vector>
#include <nlohmann/json.hpp>

namespace org::openapitools::server::model
{

/// <summary>
/// 
/// </summary>
class  Magnitude_input
{
public:
    Magnitude_input();
    virtual ~Magnitude_input() = default;


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

    bool operator==(const Magnitude_input& rhs) const;
    bool operator!=(const Magnitude_input& rhs) const;

    /////////////////////////////////////////////
    /// Magnitude_input members

    /// <summary>
    /// 
    /// </summary>
    std::vector<double> getV() const;
    void setV(std::vector<double> const value);
    bool VIsSet() const;
    void unsetv();

    friend void to_json(nlohmann::json& j, const Magnitude_input& o);
    friend void from_json(const nlohmann::json& j, Magnitude_input& o);
protected:
    std::vector<double> m_v;
    bool m_vIsSet;
    
};

} // namespace org::openapitools::server::model

#endif /* Magnitude_input_H_ */