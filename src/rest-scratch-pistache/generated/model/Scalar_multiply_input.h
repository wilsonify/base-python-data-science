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
 * Scalar_multiply_input.h
 *
 * 
 */

#ifndef Scalar_multiply_input_H_
#define Scalar_multiply_input_H_


#include <vector>
#include <nlohmann/json.hpp>

namespace org::openapitools::server::model
{

/// <summary>
/// 
/// </summary>
class  Scalar_multiply_input
{
public:
    Scalar_multiply_input();
    virtual ~Scalar_multiply_input() = default;


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

    bool operator==(const Scalar_multiply_input& rhs) const;
    bool operator!=(const Scalar_multiply_input& rhs) const;

    /////////////////////////////////////////////
    /// Scalar_multiply_input members

    /// <summary>
    /// 
    /// </summary>
    double getC() const;
    void setC(double const value);
    bool CIsSet() const;
    void unsetc();
    /// <summary>
    /// 
    /// </summary>
    std::vector<std::vector<double>> getMat() const;
    void setMat(std::vector<std::vector<double>> const& value);
    bool matIsSet() const;
    void unsetMat();

    friend void to_json(nlohmann::json& j, const Scalar_multiply_input& o);
    friend void from_json(const nlohmann::json& j, Scalar_multiply_input& o);
protected:
    double m_c;
    bool m_cIsSet;
    std::vector<std::vector<double>> m_Mat;
    bool m_MatIsSet;
    
};

} // namespace org::openapitools::server::model

#endif /* Scalar_multiply_input_H_ */
