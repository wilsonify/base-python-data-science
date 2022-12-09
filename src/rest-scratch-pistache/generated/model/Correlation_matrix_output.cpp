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


#include "Correlation_matrix_output.h"
#include "Helpers.h"

#include <sstream>

namespace org::openapitools::server::model
{

Correlation_matrix_output::Correlation_matrix_output()
{
    m_x = 0.0;
    m_xIsSet = false;
    m_Result = 0.0;
    m_ResultIsSet = false;
    
}

void Correlation_matrix_output::validate() const
{
    std::stringstream msg;
    if (!validate(msg))
    {
        throw org::openapitools::server::helpers::ValidationException(msg.str());
    }
}

bool Correlation_matrix_output::validate(std::stringstream& msg) const
{
    return validate(msg, "");
}

bool Correlation_matrix_output::validate(std::stringstream& msg, const std::string& pathPrefix) const
{
    bool success = true;
    const std::string _pathPrefix = pathPrefix.empty() ? "Correlation_matrix_output" : pathPrefix;

            
    return success;
}

bool Correlation_matrix_output::operator==(const Correlation_matrix_output& rhs) const
{
    return
    
    
    
    ((!XIsSet() && !rhs.XIsSet()) || (XIsSet() && rhs.XIsSet() && getX() == rhs.getX())) &&
    
    
    ((!resultIsSet() && !rhs.resultIsSet()) || (resultIsSet() && rhs.resultIsSet() && getResult() == rhs.getResult()))
    
    ;
}

bool Correlation_matrix_output::operator!=(const Correlation_matrix_output& rhs) const
{
    return !(*this == rhs);
}

void to_json(nlohmann::json& j, const Correlation_matrix_output& o)
{
    j = nlohmann::json();
    if(o.XIsSet())
        j["x"] = o.m_x;
    if(o.resultIsSet())
        j["result"] = o.m_Result;
    
}

void from_json(const nlohmann::json& j, Correlation_matrix_output& o)
{
    if(j.find("x") != j.end())
    {
        j.at("x").get_to(o.m_x);
        o.m_xIsSet = true;
    } 
    if(j.find("result") != j.end())
    {
        j.at("result").get_to(o.m_Result);
        o.m_ResultIsSet = true;
    } 
    
}

double Correlation_matrix_output::getX() const
{
    return m_x;
}
void Correlation_matrix_output::setX(double const value)
{
    m_x = value;
    m_xIsSet = true;
}
bool Correlation_matrix_output::XIsSet() const
{
    return m_xIsSet;
}
void Correlation_matrix_output::unsetx()
{
    m_xIsSet = false;
}
double Correlation_matrix_output::getResult() const
{
    return m_Result;
}
void Correlation_matrix_output::setResult(double const value)
{
    m_Result = value;
    m_ResultIsSet = true;
}
bool Correlation_matrix_output::resultIsSet() const
{
    return m_ResultIsSet;
}
void Correlation_matrix_output::unsetResult()
{
    m_ResultIsSet = false;
}


} // namespace org::openapitools::server::model

