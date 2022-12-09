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
 * Shape_output.h
 *
 * 
 */

#ifndef Shape_output_H_
#define Shape_output_H_


#include <nlohmann/json.hpp>

namespace org::openapitools::server::model
{

/// <summary>
/// 
/// </summary>
class  Shape_output
{
public:
    Shape_output();
    virtual ~Shape_output() = default;


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

    bool operator==(const Shape_output& rhs) const;
    bool operator!=(const Shape_output& rhs) const;

    /////////////////////////////////////////////
    /// Shape_output members

    /// <summary>
    /// 
    /// </summary>
    double getNrows() const;
    void setNrows(double const value);
    bool nrowsIsSet() const;
    void unsetNrows();
    /// <summary>
    /// 
    /// </summary>
    double getNcols() const;
    void setNcols(double const value);
    bool ncolsIsSet() const;
    void unsetNcols();

    friend void to_json(nlohmann::json& j, const Shape_output& o);
    friend void from_json(const nlohmann::json& j, Shape_output& o);
protected:
    double m_Nrows;
    bool m_NrowsIsSet;
    double m_Ncols;
    bool m_NcolsIsSet;
    
};

} // namespace org::openapitools::server::model

#endif /* Shape_output_H_ */
