{{- define "data-loader.name" -}}data-loader{{- end -}}
{{- define "data-loader.fullname" -}}{{ printf "%s-%s" .Release.Name (include "data-loader.name" .) | trunc 63 | trimSuffix "-" }}{{- end -}}
