 """ while assignedCluster < 1440:
		try:
			file_system_image = open(fs_image,"r+")
			fileCounter = 0
			for file in files:
				#Se anula el registro original
				registro = Registry("AQUI_NO_VA_NADA","13",str(file[1]),"00000000000000","00000000000000")
				file_system_image.seek(fufs.clusters[file[1]].start + file[2]*64)
				file_system_image.write(registro.name)
				file_system_image.write(registro.size)
				file_system_image.write(registro.initialCluster)
				file_system_image.write(registro.ctime)
				file_system_image.write(registro.mtime)

				registry = file[0]
				cluster = int(registry.initialCluster)
				size = registry.size
				file_system_image.seek(int(fufs.clusters[cluster].start))
				content = file_system_image.write("0"*64)
				numOfClustersUsed = math.ceil(int(size)/cluster_size)
				for i in range(registry.initialCluster,registry.initialCluster+numOfClustersUsed):
					availableClusters.append(i)

				file_system_image.seek(fufs.clusters[registryCluster].start + fileCounter*64)
				file_system_image.write(registry.name)
				file_system_image.write(registry.size)
				file_system_image.write(str(assignedCluster))
				file_system_image.write(registry.ctime)
				file_system_image.write(registry.mtime)
				fileCounter += 1
				if fileCounter % 16 == 0:
					registryCluster += 1

		file_system_image.close()

        except Exception as e:
			print(e) """