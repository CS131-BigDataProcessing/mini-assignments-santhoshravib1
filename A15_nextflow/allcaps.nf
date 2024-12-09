nextflow.enable.dsl = 2

workflow {
    processConvertToUpperCase(params.input_string)
}

process processConvertToUpperCase {
    input:
    val input_string from params.input_string

    output:
    path "output.txt"

    script:
    """
    echo "${input_string^^}" > output.txt
    """
}
}
