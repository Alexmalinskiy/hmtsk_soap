import osa


def convert_weight(value, from_unit, to_unit):
    client = osa.Client('http://www.webservicex.net/convertMetricWeight.asmx?WSDL')
    result = client.service.ChangeMetricWeightUnit(
        MetricWeightValue=value,
        fromMetricWeightUnit=from_unit,
        toMetricWeightUnit=to_unit
    )
    return float(result)


def convert_temperature(value, from_unit, to_unit):
    client = osa.Client('http://www.webservicex.net/ConvertTemperature.asmx?WSDL')
    result = client.service.ConvertTemp(
        Temperature=value,
        FromUnit=from_unit,
        ToUnit=to_unit
    )
    return float(result)


def convert_currencies(value, from_unit, to_unit, round_bool):
    client = osa.Client('http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL')
    result = client.service.ConvertToNum(
        amount=value,
        fromCurrency=from_unit,
        toCurrency=to_unit,
        rounding=round_bool
    )
    return float(result)


def convert_length(value, from_unit, to_unit):
    client = osa.Client('http://www.webservicex.net/length.asmx?WSDL')
    result = client.service.ChangeLengthUnit(
        LengthValue=value,
        fromLengthUnit=from_unit,
        toLengthUnit=to_unit,
    )
    return float(result)


def get_average_temperature(file_path):
    temperatures = []
    with open(file_path, "r", encoding="utf8") as f:
        for line in f:
            file_temperature = float(line.split(" ")[0])
            temperatures.append(convert_temperature(file_temperature, 'degreeFahrenheit', 'degreeCelsius'))
    print("{0:0.2f} Celsius degree".format(sum(temperatures)/len(temperatures)))


def get_total_costs(file_path):
    costs = []
    with open(file_path, "r", encoding="utf8") as f:
        for line in f:
            file_data = line.split(" ")
            file_costs = float(file_data[1])
            file_currency = file_data[2].strip()
            costs.append(convert_currencies(file_costs, file_currency, 'RUB', True))
    print("Total costs: {0:0.0f} RUB".format(round(sum(costs), 0)))


def get_total_length(file_path):
    length = []
    with open(file_path, "r", encoding="utf8") as f:
        for line in f:
            file_data = line.split(" ")
            file_length = float(file_data[1].replace(",", ""))
            length.append(convert_length(file_length, 'Miles', 'Kilometers'))
    print("Total length: {0:0.2f} km".format(sum(length)))


if __name__ == '__main__':
    #get_average_temperature(temps.txt)
    #get_total_costs("currencies.txt")
    get_total_length("travel.txt")
