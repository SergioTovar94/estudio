## git init

Inicializa un repositorio Git en la carpeta actual (crea la carpeta oculta .git).

## git status

Muestra el estado de los archivos:

- cuáles están modificados
- cuáles están en staging
- cuáles no están siendo seguidos

## git add .

Agrega los cambios al área de preparación (staging), listos para ser confirmados.

## git commit -m "comentario"

Guarda oficialmente los cambios en el repositorio local.

## git pull

Descarga y fusiona cambios desde el repositorio remoto hacia tu rama actual.

Internamente hace: `git fetch + git merge`

## git push

Envía los commits locales al repositorio remoto.

## git clone

Sirve para copiar un repositorio remoto a tu máquina:

`git clone url_del_repo`

## git branch

Permite ver o crear ramas.

git branch
git branch nombre_rama

## git checkout / git switch

Para cambiar de rama:

`git switch nombre_rama`

## git merge

Para unir ramas.

## git fetch

Descarga cambios del remoto sin mezclarlos automáticamente.

## git remote -v

Para ver a qué repositorio remoto estás conectado.

Muy útil cuando algo falla con push.
