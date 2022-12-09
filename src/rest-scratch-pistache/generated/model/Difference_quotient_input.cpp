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


#include "Difference_quotient_input.h"
#include "Helpers.h"

#include <sstream>

namespace org::openapitools::server::model
{

Difference_quotient_input::Difference_quotient_input()
{
    m_x = 0.0;
    m_xIsSet = false;
    m_h = 0.0;
    m_hIsSet = false;
    
}

void Difference_quotient_input::validate() const
{
    std::stringstream msg;
    if (!validate(msg))
    {
        throw org::openapitools::server::helpers::ValidationException(msg.str());
    }
}

bool Difference_quotient_input::validate(std::stringstream& msg) const
{
    return validate(msg, "");
}

bool Difference_quotient_input::validate(std::stringstream& msg, const std::string& pathPrefix) const
{
    bool success = true;
    const std::string _pathPrefix = pathPrefix.empty() ? "Difference_quotient_input" : pathPrefix;

            
    return success;
}

bool Difference_quotient_input::operator==(const Difference_quotient_input& rhs) const
{
    return
    
    
    
    ((!XIsSet() && !rhs.XIsSet()) || (XIsSet() && rhs.XIsSet() && getX() == rhs.getX())) &&
    
    
    ((!HIsSet() && !rhs.HIsSet()) || (HIsSet() && rhs.HIsSet() && getH() == rhs.getH()))
    
    ;
}

bool Difference_quotient_input::operator!=(const Difference_quotient_input& rhs) const
{
    return !(*this == rhs);
}

void to_json(nlohmann::json& j, const Difference_quotient_input& o)
{
    j = nlohmann::json();
    if(o.XIsSet())
        j["x"] = o.m_x;
    if(o.HIsSet())
        j["h"] = o.m_h;
    
}

void from_json(const nlohmann::json& j, Difference_quotient_input& o)
{
    if(j.find("x") != j.end())
    {
        j.at("x").get_to(o.m_x);
        o.m_xIsSet = true;
    } 
    if(j.find("h") != j.end())
    {
        j.at("h").get_to(o.m_h);
        o.m_hIsSet = true;
    } 
    
}

double Difference_quotient_input::getX() const
{
    return m_x;
}
void Difference_quotient_input::setX(double const value)
{
    m_x = value;
    m_xIsSet = true;
}
bool Difference_quotient_input::XIsSet() const
{
    return m_xIsSet;
}
void Difference_quotient_input::unsetx()
{
    m_xIsSet = false;
}
double Difference_quotient_input::getH() const
{
    return m_h;
}
void Difference_quotient_input::setH(double const value)
{
    m_h = value;
    m_hIsSet = true;
}
bool Difference_quotient_input::HIsSet() const
{
    return m_hIsSet;
}
void Difference_quotient_input::unseth()
{
    m_hIsSet = false;
}


} // namespace org::openapitools::server::model

