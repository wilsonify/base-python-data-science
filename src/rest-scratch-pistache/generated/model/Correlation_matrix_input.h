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
 * Correlation_matrix_input.h
 *
 * 
 */

#ifndef Correlation_matrix_input_H_
#define Correlation_matrix_input_H_


#include <vector>
#include <nlohmann/json.hpp>

namespace org::openapitools::server::model
{

/// <summary>
/// 
/// </summary>
class  Correlation_matrix_input
{
public:
    Correlation_matrix_input();
    virtual ~Correlation_matrix_input() = default;


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

    bool operator==(const Correlation_matrix_input& rhs) const;
    bool operator!=(const Correlation_matrix_input& rhs) const;

    /////////////////////////////////////////////
    /// Correlation_matrix_input members

    /// <summary>
    /// 
    /// </summary>
    std::vector<double> getX() const;
    void setX(std::vector<double> const value);
    bool XIsSet() const;
    void unsetx();
    /// <summary>
    /// 
    /// </summary>
    std::vector<double> getY() const;
    void setY(std::vector<double> const value);
    bool YIsSet() const;
    void unsety();

    friend void to_json(nlohmann::json& j, const Correlation_matrix_input& o);
    friend void from_json(const nlohmann::json& j, Correlation_matrix_input& o);
protected:
    std::vector<double> m_x;
    bool m_xIsSet;
    std::vector<double> m_y;
    bool m_yIsSet;
    
};

} // namespace org::openapitools::server::model

#endif /* Correlation_matrix_input_H_ */
