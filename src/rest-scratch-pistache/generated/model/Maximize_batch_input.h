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
 * Maximize_batch_input.h
 *
 * 
 */

#ifndef Maximize_batch_input_H_
#define Maximize_batch_input_H_


#include <vector>
#include <nlohmann/json.hpp>

namespace org::openapitools::server::model
{

/// <summary>
/// 
/// </summary>
class  Maximize_batch_input
{
public:
    Maximize_batch_input();
    virtual ~Maximize_batch_input() = default;


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

    bool operator==(const Maximize_batch_input& rhs) const;
    bool operator!=(const Maximize_batch_input& rhs) const;

    /////////////////////////////////////////////
    /// Maximize_batch_input members

    /// <summary>
    /// 
    /// </summary>
    std::vector<std::vector<double>> getX() const;
    void setX(std::vector<std::vector<double>> const& value);
    bool XIsSet() const;
    void unsetx();

    friend void to_json(nlohmann::json& j, const Maximize_batch_input& o);
    friend void from_json(const nlohmann::json& j, Maximize_batch_input& o);
protected:
    std::vector<std::vector<double>> m_x;
    bool m_xIsSet;
    
};

} // namespace org::openapitools::server::model

#endif /* Maximize_batch_input_H_ */