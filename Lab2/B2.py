# -*- coding: utf-8 -*-

def calculate_wind_chill(temperature, wind_speed):
    if wind_speed <= 3:
        return temperature
    return 35.74 + 0.6125 * temperature + (0.4275 * temperature - 35.75) * (wind_speed ** 0.16)

def process_temperature_file(input_filename, output_filename):
    try:
        # Пробуем разные кодировки
        encodings = ['cp1251', 'windows-1251', 'iso-8859-5', 'utf-8']
        lines = None
        
        for encoding in encodings:
            try:
                with open(input_filename, 'r', encoding=encoding) as file:
                    lines = file.readlines()
                print(f"Файл прочитан с кодировкой: {encoding}")
                break
            except UnicodeDecodeError:
                continue
        
        if lines is None:
            print(f"Не удалось прочитать файл {input_filename} ни в одной кодировке")
            return False
            
    except FileNotFoundError:
        print(f"Файл {input_filename} не найден")
        return False
    
    # - заголовки и пустую строка
    if len(lines) < 3:
        print("Файл слишком короткий")
        return False
        
    data_lines = lines[2:]
    
    observations = []
    total_adjusted_temp = 0
    count = 0
    
    for line in data_lines:
        line = line.strip()
        if not line:
            continue
            
        parts = line.split()
        if len(parts) >= 3:
            time = parts[0]
            try:
                temp = int(parts[1])
                wind_speed = int(parts[2])
                
                # WC температура
                wc_temp = calculate_wind_chill(temp, wind_speed)
                
                # Разница между исходной и WC температурой
                wc_effect = wc_temp - temp
                
                observations.append((time, wc_temp, wc_effect))
                total_adjusted_temp += wc_temp
                count += 1
                
            except ValueError as e:
                print(f"Ошибка в данных: {line} - {e}")
                continue
    
    # Запись результатов
    try:
        with open(output_filename, 'w', encoding='utf-8') as file:
            file.write("Time\tWC temp\tWC Effect\n")
            file.write("---\t---\t---\n")
            
            # Данные
            for time, wc_temp, wc_effect in observations:
                file.write(f"{time}\t{wc_temp:.1f}\t{wc_effect:.1f}\n")
            
            file.write("---\t---\t---\n")
            
            # Средняя температура
            if count > 0:
                avg_temp = total_adjusted_temp / count
                file.write(f"The average adjusted temperature, based on {count} observations, was {avg_temp:.1f}\n")
            else:
                file.write("No valid observations found\n")
                
        print(f" Результаты сохранены в файл: {output_filename}")
        print(f" Обработано наблюдений: {count}")
        return True
        
    except Exception as e:
        print(f" Ошибка при записи файла: {e}")
        return False

def main():
    input_file = '1.WCData.txt'
    output_file = '1.WindChiliReport.txt'
    
    print(f"Обработка файла: {input_file}")
    process_temperature_file(input_file, output_file)

if __name__ == "__main__":
    main()