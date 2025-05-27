from CPU.pipeline import Pipeline
from Test import benchmarks

def main():
    # Cargar benchmarks (puedes tener varios y elegir uno)
    programas = [benchmarks.load_program1(), benchmarks.load_program2(), benchmarks.load_program3()]
    for idx, programa in enumerate(programas, 1):
        print(f"\n===== Ejecutando Benchmark {idx} =====")
        pipeline = Pipeline(programa, cache_type="direct", cache_lines=8, block_size=4)  # Ejemplo de caché parametrizable

        max_ciclos = 105  # Límite de ciclos cambiado a 100
        while not pipeline.halted and pipeline.cycles < max_ciclos:
            print(f"\n🔄 Ciclo {pipeline.cycles + 1}")
            if hasattr(pipeline, "stall") and pipeline.stall:
                print(f"Stall detectado en ciclo {pipeline.cycles + 1}")
            pipeline.run_cycle()

        if pipeline.cycles >= max_ciclos:
            print("\n⚠️ Se alcanzó el límite de ciclos. Posible bucle infinito.")

        print("\n✅ Simulación completada")
        print(f"Ciclos ejecutados: {pipeline.cycles}")

        # Mostrar registros (primeros 8)
        if hasattr(pipeline, "registers"):
            reg_list = pipeline.registers[:100]
            print(f"Registros: {reg_list}")

        # Estadísticas de caché
        if hasattr(pipeline, "cache") and pipeline.cache:
            print("\n📊 Estadísticas de Caché:")
            stats = pipeline.cache.get_stats()
            for k, v in stats.items():
                if k == "hit_rate":
                    print(f"{k}: {v:.2f}")
                else:
                    print(f"{k}: {v}")

        # Estadísticas de E/S (si implementas E/S)
        if hasattr(pipeline, "io_stats"):
            print("\n📟 Estadísticas de E/S:")
            for k, v in pipeline.io_stats.items():
                print(f"{k}: {v}")

if __name__ == "__main__":
    main()