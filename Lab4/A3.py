packets = str(input())
length = len(packets)

if not all(char in '01' for char in packets):
    print("Неверный ввод. Используйте только символы '0' и '1'!")
else:
    if length < 5:
        print("Последовательность слишком короткая! Нужно минимум 5")
    else:
        all_packets = length
        max_zeros = 0
        current_zeros = 0

        for char in packets:
            if char == '0':
                current_zeros += 1
                max_zeros = max(max_zeros, current_zeros)
            else:
                current_zeros = 0
        
        invalid_packets = packets.count('0')
        procent_invalid = invalid_packets / length * 100

        if procent_invalid <= 1:
            quality = 'Отличное качество'
        elif procent_invalid > 1 and procent_invalid <= 5:
            quality = 'Хорошее качество'
        elif procent_invalid > 5 and procent_invalid <= 10:
            quality = 'Удовлетворительное качество'
        elif procent_invalid > 10 and procent_invalid <= 20:
            quality = 'Плохое качество'
        else:
            quality = 'Критическое состояние сети'

        print(f'• Общее количество пакетов: {length}\n',
            f'• Количество потерянных пакетов: {invalid_packets}\n',
            f'• Длина самой длинной последовательности потерянных пакетов: {max_zeros}\n',
            f'• Процент потерь: {procent_invalid:.2f}%\n',
            f'• Качество связи: {quality}\n')